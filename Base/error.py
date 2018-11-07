""" 180222 Adel Liu

错误表，在编码时不断添加
"""


class E:
    _error_id = 0

    def __init__(self, msg, release_e=None):
        self.eid = E._error_id
        self.msg = msg
        self.release = release_e if isinstance(release_e, E) else None
        E._error_id += 1


class Error:
    OK = E("没有错误")
    REQUIRE_PARAM = E("缺少参数")
    REQUIRE_JSON = E("需要JSON数据")
    STRANGE = E("未知错误")
    ERROR_METHOD = E("错误的HTTP请求方法")
    REQUIRE_BASE64 = E("参数需要base64编码")
    ERROR_PARAM_FORMAT = E("错误的参数格式")
    ERROR_VALIDATION_FUNC = E("错误的参数验证函数")
    ERROR_PROCESS_FUNC = E("错误的预处理函数")

    UNRESOLVED_LINK = E("无法解析的链接")
    ERROR_HANDLER = E("处理错误")
    NEW_VERSION_SUPPORT = E("新版本支持下载此视频")
    NO_URL = E("找不到URL链接")

    @classmethod
    def get_error_dict(cls):
        error_dict = dict()
        for k in cls.__dict__:
            if k[0] != '_':
                e = getattr(cls, k)
                if isinstance(e, E):
                    error_dict[k] = dict(eid=e.eid, msg=e.msg)
        return error_dict

