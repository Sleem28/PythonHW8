import csv
import os

w_path = os.path.join('GUI', 'Export', 'DataBase', 'phonebook.html')
r_path = os.path.join('GUI', 'Export', 'DataBase', 'phonebook.csv')


def export_file_to_html():
    with open(w_path, 'w') as html_page:
        style = 'style="font-size:22px;"'
        html = '<html>\n  <head></head>\n  <body>\n'

        with open (r_path, encoding='utf-8') as r_file:
            reader = csv.reader(r_file, delimiter=';')
            counter = 0

            for row in reader:
                if counter == 0: 
                    f_name = row[0]
                    l_name = row[1]
                    phone  = row[2]
                    adr    = row[3]
                else:
                    html += f'    <p {style}>{f_name} = {row[0]}, {l_name} = {row[1]}, {phone} = {row[2]}, {adr} = {row[3]}</p>\n' if len(row) >=4 else \
                            f'    <p {style}> info_error</p>'

                counter += 1
        html += '  </body>\n</html>'
        html_page.write(html)

        return html

