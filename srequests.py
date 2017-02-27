#!/usr/bin/env python

import requests
import socket
import ssl


from urlparse import urlparse


def request_to_string(req):
    prepared = req.prepare();
    prepared.prepare_headers(req.headers)
    prepared.prepare_content_length(prepared.body)
    prepared.prepare_body(req.data, req.files)

    path = '/'
    p = urlparse(req.url)
    if p.path:
        path = p.path

    body = prepared.body
    prepared.headers['Host'] = urlparse(req.url).netloc

    request_string = '{}\r\n{}\r\n\r\n{}'.format(
        prepared.method + ' ' + path + ' ' + 'HTTP/1.1',
        '\r\n'.join('{}: {}'.format(k, v) for k, v in prepared.headers.items()),
        body
    )
    return request_string


def srequest(method, url, bind_port=31337, **kwargs):
    #TODO: Add tls support
    prepared_request = requests.Request(method, url, **kwargs)
    request_string   = request_to_string(prepared_request)

    o = urlparse(url)
    default_ports = {"http": 80, "https":443}


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', bind_port))
    s.settimeout(30)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((o.hostname, o.port or default_ports[o.scheme]))
    s.send(request_string)

    return s


def get(url, bind_port=31337, **kwargs):
    return srequest("GET", url, bind_port=bind_port, **kwargs)


def post(url, bind_port=31337, **kwargs):
    return srequest("POST", url, bind_port=bind_port, **kwargs)


def head(url, bind_port=31337, **kwargs):
    return srequest("DELETE", url, bind_port=bind_port, **kwargs)


def put(url, bind_port=31337, **kwargs):
    return srequest("PUT", url, bind_port=bind_port, **kwargs)


def patch(url, bind_port=31337, **kwargs):
    return srequest("PATCH", url, bind_port=bind_port, **kwargs)


def delete(url, bind_port=31337, **kwargs):
    return srequest("DELETE", url, bind_port=bind_port, **kwargs)
