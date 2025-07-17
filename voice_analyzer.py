# -*- coding: utf-8 -*-
#################################################################################
#   OpenERP, Open Source Management Solution
#   Copyright (C) Andrzej Wiśniewski[a.wisniewski@yourwebdesign.be].
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#   2025(c) Andrzej Wisniewski
#
#################################################################################
import sys
import os
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import gettext

from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import MidTermFeatures
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

# --- Setup translation ---
def setup_translation(lang_code='pl'):
	try:
		lang = gettext.translation('messages', localedir='locale', languages=[lang_code])
		lang.install()
		return lang.gettext
	except FileNotFoundError:
		print(f"⚠️ Brak tlumaczenia dla jezyka '{lang_code}', uzywam domyslnego.")
		return lambda s: s

# --- Feature Extraction ---
def analyze_audio_file(file_path):
	[Fs, x] = audioBasicIO.read_audio_file(file_path)
	if x.ndim > 1:
		x = x[:, 0]
	mt_features, _, feature_names = MidTermFeatures.mid_feature_extraction(
		x, Fs, 1.0, 1.0, 0.050, 0.050
	)
	feature_means = np.mean(mt_features, axis=1)
	return dict(zip(feature_names, feature_means))

# --- MFCC Plot ---
def generate_mfcc_plot(audio_path, output_image="mfcc_plot.png"):
	y, sr = librosa.load(audio_path, sr=None)
	mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
	plt.figure(figsize=(10, 4))
	librosa.display.specshow(mfcc, x_axis='time', sr=sr)
	plt.colorbar(label='MFCC Value')
	plt.title('MFCC Coefficients Over Time')
	plt.tight_layout()
	plt.savefig(output_image)
	plt.close()
	return output_image

# --- PDF Report ---
def generate_pdf_report(features, input_file, mfcc_image, analyst_name, analyst_email, case_id, lang_code):
	_ = setup_translation(lang_code)
	now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	suspicious = []
	if features.get("zcrMean", 0) < 0.01:
		suspicious.append(_("Very low zero-crossing (possible synthesis)"))
	if features.get("mfcc_1_mean", 0) < -500:
		suspicious.append(_("Unnatural spectral shape (low MFCC_1)"))

	c = canvas.Canvas("report.pdf", pagesize=A4)
	width, height = A4

	c.setFont("Helvetica-Bold", 14)
	c.drawString(2 * cm, height - 2 * cm, _("TECHNICAL REPORT - AUDIO ANALYSIS"))
	c.setFont("Helvetica", 10)
	c.drawString(2 * cm, height - 2.8 * cm, f"{_('Analysis date')}: {now}")
	c.drawString(2 * cm, height - 3.4 * cm, f"{_('Input file')}: {input_file}")
	c.drawString(2 * cm, height - 4.0 * cm, f"{_('Case ID')}: {case_id}")
	c.drawString(2 * cm, height - 4.6 * cm, f"{_('Analyst')}: {analyst_name}")
	c.drawString(2 * cm, height - 5.2 * cm, f"{_('Email')}: {analyst_email}")

	c.drawString(2 * cm, height - 6.2 * cm, _("Heuristic Evaluation:"))
	y_pos = height - 6.8 * cm
	if suspicious:
		for s in suspicious:
			c.drawString(2.5 * cm, y_pos, f"- {s}")
			y_pos -= 0.4 * cm
	else:
		c.drawString(2.5 * cm, y_pos, _("No suspicious features found"))

	y_pos -= 1.0 * cm
	c.setFont("Helvetica-Bold", 11)
	c.drawString(2 * cm, y_pos, _("Acoustic Features (averaged):"))
	y_pos -= 0.5 * cm
	c.setFont("Courier", 9)
	for name, value in features.items():
		if y_pos < 4 * cm:
			c.showPage()
			y_pos = height - 3 * cm
		c.drawString(2.5 * cm, y_pos, f"{name:30s} : {value:.4f}")
		y_pos -= 0.35 * cm

	c.showPage()
	c.setFont("Helvetica-Bold", 12)
	c.drawString(2 * cm, height - 2 * cm, _("MFCC Visualization"))
	c.drawImage(mfcc_image, 2 * cm, 4 * cm, width=16 * cm, preserveAspectRatio=True, mask='auto')
	c.setFont("Helvetica", 8)
	c.drawString(2 * cm, 2 * cm, _("Disclaimer: This report is for informational use only and is not a forensic expert opinion."))
	c.save()
	print("✅ Report saved as report.pdf")

# --- Entry point ---
if __name__ == "__main__":
	if len(sys.argv) < 6:
		print("Usage: python3 voice_analyzer.py <audio_file> <CASE_ID> <ANALYST_NAME> <EMAIL> <LANG_CODE>")
		sys.exit(1)

	input_file = sys.argv[1]
	case_id = sys.argv[2]
	analyst_name = sys.argv[3]
	analyst_email = sys.argv[4]
	lang_code = sys.argv[5]

	if not os.path.isfile(input_file):
		print("❌ Audio file not found.")
		sys.exit(1)

	features = analyze_audio_file(input_file)
	mfcc_image = generate_mfcc_plot(input_file)
	generate_pdf_report(features, input_file, mfcc_image, analyst_name, analyst_email, case_id, lang_code)

#EoF
