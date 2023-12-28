from urllib.parse import urlparse, urlunparse, urlencode

def build_url(base_url, path, args_dict):
    # Возвращает список в структуре urlparse.ParseResult
    url_parts = list(urlparse(base_url))
    url_parts[2] = path
    url_parts[4] = urlencode(args_dict)
    return urlunparse(url_parts)

# Пример использования build_url
args = {'arg1': 'value1', 'arg2': 'value2'}

# Работает со сценарием двойной косой черты
url1 = build_url('http://www.example.com/', '/somepage/index.html', args)
print(url1)
# Вывод: http://www.example.com/somepage/index.html?arg1=value1&arg2=value2

# Работает без косой черты
url2 = build_url('http://www.example.com', 'somepage/index.html', args)
print(url2)
# Вывод: http://www.example.com/somepage/index.html?arg1=value1&arg2=value2


# Пример использования urlparse для разбора URL-адреса и изменения протокола
url_to_parse = "//www.cwi.nl:80/%7Eguido/Python.html"
parsed_url = urlparse(url_to_parse, scheme='http')  # Указываем протокол по умолчанию

print(parsed_url)
# Вывод: ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html', params='', query='', fragment='')

# Пример изменения протокола
modified_url = parsed_url._replace(scheme='https')
print(urlunparse(modified_url))
# Вывод: https://www.cwi.nl:80/%7Eguido/Python.html
