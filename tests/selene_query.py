from selene.support.conditions import have
from selene.support.shared import browser
from selene.support.jquery_style_selectors import s
from selene.support.shared.jquery_style import ss


def test_query_complete():
    browser.open('http://todomvc.com/examples/emberjs/')

    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()

    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

    browser.all('#todo-list>li').element_by(have.exact_text('b')).element('.toggle').click()
    browser.all('#todo-list>li').filtered_by(have.css_class('completed')).should(have.exact_texts('b'))
    browser.all('#todo-list>li').filtered_by(have.no.css_class('completed')).should(have.exact_texts('a', 'c'))





