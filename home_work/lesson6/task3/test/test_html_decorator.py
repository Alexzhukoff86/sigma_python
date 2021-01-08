from home_work.lesson6.task3.source.html_decorator import html_element


def test_html_decorator():
    assert html_element(">list_item<") == ['<li>List item 1</li>', '<li>List item 2</li>', '<li>List item 3</li>']