from selene.support.shared import browser
from selene import have, command

todo_list = browser.all('#todo-list>li')

def visit():
    browser.open('https://todomvc4tasj.herokuapp.com/')
    app_wait = "return $._data($('#clear-completed')[0], 'events')"\
               ".hasOwnProperty('click')"
    browser.should(have.js_returned(True, app_wait))

def add(*tasks: str):
    for todo in tasks:
        browser.element('#new-todo').type(todo).press_enter()

def assert_list(*tasks: str):
    todo_list.should(have.exact_texts(*tasks))

def start_editing(todo: str, new_text):
    todo_list.element_by(have.exact_text(todo)).double_click()
    return todo_list.element_by(have.css_class('editing')).element('.edit')\
        .perform(command.js.set_value(new_text))

def edit(todo: str, new_text):
    start_editing(todo, new_text).press_enter()

def cancel_editing(todo: str, new_text):
    start_editing(todo, new_text).press_escape()

def toggle(todo: str):
    todo_list.element_by(have.exact_text(todo)).element('.toggle').click()

def clear_completed():
    browser.element('#clear-completed').click()

def delete(todo: str):
    todo_list.element_by(have.exact_text(todo)).hover()\
        .element('.destroy').click()
