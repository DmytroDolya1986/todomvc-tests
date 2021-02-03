from todomvc_tests.test_app import app


def test_primal_app_functionality():
    app.entry()

    app.add('a', 'b', 'c')
    app.assert_list('a', 'b', 'c')

    app.edit('b', 'b edited')

    app.switch('b edited')

    app.clear_completed()
    app.assert_list('a', 'c')

    app.cancel_editing('c', 'to be canceled')

    app.destroy('c')
    app.assert_list('a')
