import page

def test_textoveho_prvku_na_strance_go_to_jobs(page):
    page.goto('https://www.usu.com/en-us/')

    accept_button = page.get_by_role("button", name="Accept all")
    accept_button.click()

    careers = page.locator('a.top__extra-link[href="/en-us/company/careers/"]')
    careers.click()

    go_to_jobs = page.locator('(//a[@class="knob" and @href="/en-us/company/careers/jobs/"])[1]')
    go_to_jobs.click()

   #Kontrola textového prvku "What are you looking for?"

    text_element = page.locator("h2.listing__title")
    text_element.wait_for(state="visible")

    assert text_element.inner_text() == "What are you looking for?"

    page.close()


def test_prihlasovani_odhlasovani_na_strance_rohlikcz(page):
    page.goto('https://www.rohlik.cz/')

    accept_button = page.get_by_role("button", name="Povolit všechny")
    accept_button.click()

    account_button = page.locator('[data-test="header-user-icon"] button[data-test="button"]')
    account_button.click()

    #Prihlaseni
    email_input = page.locator('input[data-test="input"][id="email"]')
    email_input.fill("a.kocirova@gmail.com")
    pasword_input = page.locator('input[data-test="input"][id="password"]')
    pasword_input.fill("Vineclub13")
    login_button = page.locator('button[data-test="btnSignIn"][type="submit"]')
    login_button.click()

    #Odhlaseni
    element_ak = page.locator('div.sc-50e32369-6')
    element_ak.click()
    element_odhlasit_se = page.locator('a.logOut[data-test="user-box-logout-button"]')
    element_odhlasit_se.click()

    page.close()



def test_udaju_na_strance_pocasicz(page):
    page.goto('https://www.pocasi.cz/')

    #Logo "Počasí.cz"
    logo_element = page.locator('a[data-dot="ogm-header-logo"]')
    logo_element.wait_for(state="visible")

    assert logo_element.inner_text() == "Počasí.cz"

    expected_width = 147
    expected_height = 30

    bounding_box = logo_element.bounding_box()
    assert bounding_box is not None, "Bounding box is None"
    actual_width = bounding_box['width']
    actual_height = bounding_box['height']


    #Text "Počasí v České republice"
    text_element = page.locator('h2.b_gg.b_ab.c_gm:has-text("Počasí v České republice")')
    text_element.wait_for(state="visible")

    assert text_element.inner_text() == "Počasí v České republice"

    expected_width = 631
    expected_height = 28

    bounding_box = text_element.bounding_box()
    assert bounding_box is not None, "Bounding box is None"
    actual_width = bounding_box['width']
    actual_height = bounding_box['height']

    #Vyhledávač a tlačítko vyhledat
    search_input = page.locator('input[data-dot="lista_hledani_kurzor"][name="ribbon--search"]')
    search_input.wait_for(state="visible")


    expected_width = 272.13
    expected_height = 40

    bounding_box = text_element.bounding_box()
    assert bounding_box is not None, "Bounding box is None"
    actual_width = bounding_box['width']
    actual_height = bounding_box['height']



    search_input.fill("Prostějov")
    button = page.locator('button[data-dot="lista_hledani_button"]')
    button.wait_for(state="visible")
    button.click()

    page.close()
