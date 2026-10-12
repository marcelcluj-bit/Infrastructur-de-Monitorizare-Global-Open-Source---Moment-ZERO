import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.units import inch

def generate_opml():
    """Generates the OPML file containing global primary RSS feeds."""
    opml_content = """<?xml version="1.0" encoding="UTF-8"?>
<opml version="2.0">
  <head>
    <title>MOMENT ZERO - Fluxuri Globale</title>
  </head>
  <body>
    <outline text="GLOBAL" title="GLOBAL">
      <outline type="rss" text="Reuters World" xmlUrl="https://www.reutersagency.com/feed/" />
      <outline type="rss" text="BBC News" xmlUrl="http://feeds.bbci.co.uk/news/world/rss.xml" />
      <outline type="rss" text="Al Jazeera" xmlUrl="https://www.aljazeera.com/xml/rss/all.xml" />
      <outline type="rss" text="DW News" xmlUrl="https://rss.dw.com/rdf/rss-en-all" />
    </outline>
  </body>
</opml>"""
    
    with open("surse_moment_zero.opml", "w", encoding="utf-8") as f:
        f.write(opml_content)
    print("✓ Fișierul OPML a fost generat: surse_moment_zero.opml")

def generate_pdf():
    """Generates the official presentation PDF using ReportLab."""
    file_name = "Prezentare_Moment_Zero_Oficial.pdf"
    doc = SimpleDocTemplate(
        file_name, 
        pagesize=A4,
        rightMargin=72, 
        leftMargin=72, 
        topMargin=72, 
        bottomMargin=72
    )
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=24,
        textColor=colors.black,
        alignment=1,
        spaceAfter=6
    )

    subtitle_style = ParagraphStyle(
        'SubtitleStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        textColor=colors.grey,
        alignment=1,
        spaceAfter=20
    )

    header_style = ParagraphStyle(
        'HeaderStyle',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        spaceBefore=12,
        spaceAfter=10,
        textColor=colors.black,
        borderPadding=2,
    )

    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=14,
        alignment=4,
        spaceAfter=10
    )

    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=14,
        leftIndent=20,
        firstLineIndent=0,
        spaceAfter=8
    )

    footer_style = ParagraphStyle(
        'FooterStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        textColor=colors.grey,
        alignment=1,
        spaceBefore=5
    )

    elements = []

    # Title & Subtitle
    elements.append(Paragraph("MOMENT ZERO", title_style))
    elements.append(Paragraph("Infrastructură de Monitorizare Globală pentru Redacții și Lideri", subtitle_style))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.black, spaceAfter=20))

    # Misiunea
    elements.append(Paragraph("🎯 MISIUNEA", header_style))
    elements.append(Paragraph("Eliminarea zgomotului algoritmic și a manipulării prin oferirea unui acces direct la sursele primare de informație de pe 5 continente, într-un format curat, rapid și fără perturbări publicitare.", body_style))
    elements.append(Spacer(1, 12))

    # Capabilități Tehnice
    elements.append(Paragraph("🛠 CAPABILITĂȚI TEHNICE", header_style))
    data = [
        [Paragraph("<b>Pilon</b>", body_style), Paragraph("<b>Descriere</b>", body_style)],
        [Paragraph("Agregare Globală", body_style), Paragraph("Acces la fluxuri brute din SUA, UE, Rusia, China, India și Lumea Arabă.", body_style)],
        [Paragraph("Multimodalitate", body_style), Paragraph("Integrare TV Live, Presă Scrisă, Podcast-uri și Social Media într-un singur Hub.", body_style)],
        [Paragraph("Autenticitate", body_style), Paragraph("Titluri în limba originală cu traducere tehnică (italice) pentru zero bias.", body_style)],
        [Paragraph("Incluziune AI", body_style), Paragraph("Modul opțional Audio și analize comparative automate între surse.", body_style)]
    ]

    t = Table(data, colWidths=[1.4*inch, 4.3*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.lightgrey),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 18))

    # Avantaje Redacții
    elements.append(Paragraph("🚀 AVANTAJE PENTRU REDACȚII", header_style))
    elements.append(Paragraph("• <b>Viteză de Reacție:</b> Monitorizare în timp real, înainte de traducerile oficiale.", bullet_style))
    elements.append(Paragraph("• <b>Eficiență:</b> Un singur dashboard pentru scanarea întregii planete.", bullet_style))
    elements.append(Paragraph("• <b>Zero Costuri Mentenanță:</b> Sistem Open Source bazat pe WordPress, auto-actualizat.", bullet_style))
    elements.append(Paragraph("• <b>Neutralitate:</b> Posibilitatea de a compara perspectivele Est vs. Vest instantaneu.", bullet_style))
    elements.append(Spacer(1, 12))

    # Filozofia Zero
    elements.append(Paragraph("🛡 FILOZOFIA ZERO", header_style))
    elements.append(Paragraph("Proiectul este ghidat de patru piloni de integritate: <b>Zero Reclame</b>, <b>Zero Cookie-uri</b> (nu colectăm date), <b>Zero Tracking</b> și <b>Zero Costuri</b> pentru utilizatorul final.", body_style))

    # Implementare
    elements.append(Paragraph("📥 IMPLEMENTARE ȘI DISTRIBUȚIE", header_style))
    elements.append(Paragraph("1. Descărcați pachetul de configurare (Template WordPress + Listă Surse OPML).", bullet_style))
    elements.append(Paragraph("2. Instalați arhiva pe domeniul propriu (ex: hub.ziarul-tau.ro).", bullet_style))
    elements.append(Paragraph("3. Activați cheia AI (opțional) pentru funcțiile de traducere și audio.", bullet_style))

    # Footer
    elements.append(Spacer(1, 40))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey))
    elements.append(Paragraph("\"Informația de la sursă este singura apărare în era dezinformării.\"", footer_style))
    elements.append(Paragraph("Proiectul MOMENT ZERO - Licență Public Domain", footer_style))

    doc.build(elements)
    print("✓ Fișierul PDF a fost generat: Prezentare_Moment_Zero_Oficial.pdf")

if __name__ == "__main__":
    print("Pornire proces generare resurse MOMENT ZERO...")
    generate_opml()
    generate_pdf()
    print("Toate resursele au fost create cu succes!")
