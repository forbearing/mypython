1:
    1:在发送请求后，得到的是响应，我们使用 text 和 content 获取了响应的内容，此外，还有很多属性
      和方法可以用来获取其他信息。比如状态码、响应头、Cookies 等

    import requests
    r = requests.get('http://jianshu.com')
    print(type(r.status_code),r.status_code)
    print(type(r.headers), r.headers)
    print(type(r.cookies), r.cookies)
    print(type(r.url), r.url)
    print(type(r.history), r.history)


2:状态码
    1:requests 提供了一个内置的状态码查询对象 requests.codes

    import requests
    r = requests.get('http://www.jianshu.com')
    exit() if not r.status_code == requests.codes.ok else print('Request Successfully')
    # 通过比较返回码和内置的成功状态码，来保证请求得到了正常的响应

    2:信息状态码
        100:    ('continue',),
        101:    ('switching_protocols',),
        102:    ('processing',),
        103:    ('checkpoint',),
        122:    ('uri_too_long', 'request_uri_too_long'),
    3:成功状态码
        200:    ('ok', 'okay', 'all_ok', 'all_okay', 'all_good', '\\0/'),
        201:    ('created',),
        202:    ('accepted',),
        203:    ('non_authoritative_info', 'non_authoritative_information'),
        204:    ('no_content',),
        205:    ('reset_content', 'reset')
        206:    ('partial_content', 'partial')
        207:    ('multi_status', 'multiple_status', 'multi_stati', 'multiple_stati')
        208:    ('already_reported')
        226:    ('im_used')
    3:重定向状态码
        300:    ('multiple_choices')
        301:    ('moved_permanently', 'moved', '\\o-')
        302:    ('found')
        303:    ('see_other', 'other')
        304:    ('not_modified')
        305:    ('use_proxy')
        306:    ('switch_proxy')
        307:    ('temporary_redirect', 'temporary_moved', 'temporary')
        308:    ('permanent_redirect', 'resume_incomplete', 'resume')
    4:客户端错误状态码
        400:    ('bad_request', 'bad')
        401:    ('unauthorized')
        402:    ('payment_required', 'payment')
        403:    ('forbidden')
        404:    ('not_found', '-o-')
        405:    ('method_not_allowed', 'not_allowed')
        406:    ('not_acceptable')
        407:    ('proxy_authentication_required','proxy_auth','proxy_authentication')
        408:    ('request_timeout', 'timeout')
        409:    ('conflict')
        410:    ('gone')
        411:    ('length_required')
        412:    ('precondition_failed', 'precondition')
        413:    ('request_entity_too_large')
        414:    ('request_uri_too_large')
        415:    ('unsupported_media_type', 'unsupported_media', 'media_type')
        416:    ('requested_range_not_satisfiable', 'requested_range', 'range_not_satisfiable')
        417:    ('expectation_failed')
        418:    ('im_a_teapot', 'teapot', 'i_am_a_teapot')
        421:    ('misdirected_request')
        422:    ('unprocessable_entity', 'unprocessable')
        423:    ('locked')
        424:    ('failed_dependency', 'dependency')
        425:    ('unordered_collection', 'unordered')
        426:    ('upgrade_required', 'upgrade')
        428:    ('precondition_required', 'precondition')
        429:    ('too_many_requests', 'too_many')
        431:    ('header_fields_too_large', 'fields_too_large')
        444:    ('no_response', 'none')
        449:    ('retry_with', 'retry')
        451:    ('unavailable_for_legal_reasons', 'legal_reasons')
        499:    ('client_closed_request')
    5:服务器错误状态码
        500:    ('internal_server_error', 'server_error', '/o\\')
        501:    ('not_implemented')
        502:    ('bad_geteway')
        503:    ('service_unavailable', 'unavailable')
        504:    ('gateway_timeout')
        505:    ('http_version_not_supported', 'http_version')
        506:    ('variant_also_negotiates')
        507:    ('insufficient_storage')
        509:    ('bandwidth_limit_exceeded', 'bandwidth')
        510:    ('not_extended')
        511:    ('network_authentication_required', 'network_auth', 'network_authentication')

