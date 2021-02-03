from selene.support.shared import browser
from selene import have, command

todo_list = browser.all('#todo-list>li')

def entry():
    browser.open('https://todomvc4tasj.herokuapp.com/')
    app_wait = "return $._data($('#clear-completed')[0], 'events')"\
               ".hasOwnProperty('click')"
    browser.should(have.js_returned(True, app_wait))

def add(*task: str):
    for todo in task:
        browser.element('#new-todo').type(todo).press_enter()

def assert_list(*task: str):
    todo_list.should(have.exact_texts(*task))

def start_editing(todos: str, new_text):
    todo_list.element_by(have.exact_text(todos)).double_click()
    return todo_list.element_by(have.css_class('editing')).element('.edit')\
        .perform(command.js.set_value(new_text))

def edit(todos: str, new_text):
    start_editing(todos, new_text).press_enter()

def cancel_editing(todos: str, new_text):
    start_editing(todos, new_text).press_escape()

def switch(todos: str):
    todo_list.element_by(have.exact_text(todos)).element('.toggle').click()

def clear_completed():
    browser.element('#clear-completed').click()

def destroy(todos: str):
    todo_list.element_by(have.exact_text(todos)).hover()\
        .element('.destroy').click()
