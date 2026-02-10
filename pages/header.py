def switch_language(page, language):
    language_text = {"en": "English", "ru": "Русский", "ka": "ქართული"}
    page.locator("#language-toggle").click()
    page.locator("#language-dropdown div div").filter(
        has=page.locator("span", has_text=language_text[language])
    ).click()