from todomvc_tests.model import todo


def test_primal_app_functionality():
    todo.visit()

    todo.add('a', 'b', 'c')
    todo.assert_list('a', 'b', 'c')

    todo.edit('b', 'b edited')

    todo.toggle('b edited')

    todo.clear_completed()
    todo.assert_list('a', 'c')

    todo.cancel_editing('c', 'to be canceled')

    todo.delete('c')
    todo.assert_list('a')
