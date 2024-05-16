from selene.support import by


class App:
    search_field = by.css('[name="q"]')
    search_list_found = by.css('[id="search"]')
    search_list_empty = by.css('[class="card-section"')