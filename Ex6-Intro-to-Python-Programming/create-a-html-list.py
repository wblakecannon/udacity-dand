'''
Quiz: Create an HTML List
Write the html_list function. The function takes one argument, a list of strings, and returns a
single string which is an HTML list. For example, if the function should produce the following
string when provided the list ['first string', 'second string'].

<ul>
<li>first string</li>
<li>second string</li>
</ul>
That is, the string's first line should be the opening tag <ul>. Following that is one line per
element in the source list, surrounded by <li> and </li> tags. The final line of the string should
be the closing tag </ul>.

My solution:
'''
def html_list(string_list):
    new_html_list = []
    for element in string_list:
        element = '<li>' + element + '</li>'
        new_html_list.append(element)
    new_html_list.insert(0, '<ul>')
    new_html_list.append('</ul>')
    new_html_list = '\n'.join(new_html_list)
    return new_html_list

print(html_list(['first string', 'second string']))

'''
Udacity Solution:
Your code passes all of our tests, nice work!

This is our solution:

def html_list(list_items):
    HTML_string = "<ul>\n"
    for item in list_items:
        HTML_string += "<li>{}</li>\n".format(item)
    HTML_string += "</ul>"
    return HTML_string
'''