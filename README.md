# README

1. **What It Does**  
   - Reads **`bib_test.bib`**.  
   - Appends unique IDs to repeated references (from the `checks` list).  
   - Replaces overly long author lists with generic placeholders.  
   - Outputs the final references to **`bib.bib`**.
   - Large author entries become {The CMS Collaboration}, {The CMS GEM Group}, or {The Muon Collider Collaboration} depending on line length.

2. **Setup**  
   - Place your `.bib` file in this folder and name it **`bib_test.bib`**.  
   - Make sure the `checks` list has all the labels you want to disambiguate.
     - If you see any missed duplicates or new repeated labels, add them to checks.
   - Remove all the temporay file in particular the bibliography.pdf
     - Also `bib.bib` can be removed

3. **Usage**  
   - ```python organize_orcid.py```
   - The script will process bib_test.bib and create/overwrite bib.bib with cleaned references.
   - now build the bibliography.tex