# 3D-Object-Tracking-Documentation

## Resources

- Moodle-Kurs "HÖHERE: Vorlagen Diplomarbeit"
- [Bundesministerium Bildung](https://www.diplomarbeiten-bbs.at/)

## Typical documentation structure

- Title Page (Titelblatt)
- Abstract/Summary (Abstract/Zusammenfassung)
- Table of Contents (Inhaltsverzeichnis)
- List of Abbreviations (optional) (Abkürzungsverzeichnis (optional))
- List of Figures (Abbildungsverzeichnis)
- List of Tables (Tabellenverzeichnis)
- Introduction/Motivation (Einleitung/Motivation)
- State of the Art (Stand der Technik)
- Methods (Methoden)
- Results (Ergebnisse)
- Discussion (Diskussion)
- Conclusion (Schlussfolgerung)
- Outlook (Ausblick)
- Acknowledgements (Danksagung)
- References/Bibliography (Referenzen/Literaturliste)
- Appendices (Anhänge)

## File Structure

```
├── content
│   ├── abstract.tex            Hier kommen das deutsche und englische Abstract rein
│   ├── einleitung.tex          Grundsätzliches zur gesamten Arbeit, auch indiv. Aufteilung der Arbeiten
│   └── latex_beispiele.tex     Grundsätzliche Latex-Funktionalität wird hier gezeigt 
├── figures
│   ├── bsp.png
│   ├── htl-logo2.png
│   └── htl-logo.png
├── main.tex                    Hier läuft alles zusammen. Dort ist auch Thema, Betreuer, Abteilung, Jahr usw. einzutragen
├── references.bib              Alle Zitate befinden sich hier. In latex_beispiele wird gezeigt wie man diese einbindet
├── sourcecode
│   └── First.java
├── template
│   ├── affirmation.tex         Eidesstattliche Erklärung
│   ├── listing_format.tex      Wie soll der Quellcode formatiert werden? Anwendung dazu in content/latex_beispiele
│   ├── lock_flag.tex           Falls ein Sperrvermerk gemacht werden soll, dieses file einblenden bzw. ausblenden (in main.tex)
│   ├── main_settings.tex       Grundsätzliches zum Basislayout. Hier sollte man wenig ändern müssen
│   ├── mycommands.tex          Bestimmte Befehle werden hier überschrieben für einheitliches Layout. Hier sollte man wenig ändern müssen
│   ├── pdf_settings.tex        Parameter für die PDF-Generierung. Hier sollte man wenig ändern müssen
│   ├── preamble.tex            Hier kommen die ganzen imports hin
│   ├── title_thesis_htlinn.tex Das Titelblatt, hier werden die Infos von main.tex eingebaut
│   └── typographic_settings.texHier sollte man wenig ändern müssen
```

> Quelle: Moodle-Kurs "HÖHERE: Vorlagen Diplomarbeit"


## Known problems

```
Möchte man dass der Inhalt der ersten Seite wirklich genau in der Mitte liegt und die Folgeseiten die Ränder für ein 2-seitiges Layout anpasst

% Festlegen des grundlegenden Layouts (Ränder auch in cm angebbar)
\usepackage[oneside, left=1in, right=1in, top=1in, bottom=1in]{geometry}

\begin{document}
% Content of the first page


% Jetzt schalten wir wieder zurück auf twopage
\newgeometry{twoside, left=1in, right=1in, top=1in, bottom=1in, bindingoffset=0.5in}

% The rest of your document goes here

\end{document}



Die Tabelle mit der Zeitangabem am Ende schreibt in den Footer

Lösung: Verwendung einer Longtable anstatt einer normalen Tabelle

\usepackage{longtable}

\begin{longtable}
...
\end{longtable}

Zuletzt geändert: Donnerstag, 14. März 2024, 16:24
```

> Quelle: Moodle-Kurs "HÖHERE: Vorlagen Diplomarbeit"
