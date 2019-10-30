

class Opts:
    ZSXQ_ACCESS_TOKEN = '065D0868-C6A3-B41E-75D5-42DD7EC1AD96'  # 登录后Cookie中的Token
    GROUP_ID = '15285211242422'  # 知识星球中的小组ID 141281112142  每日分享554228114224
    PDF_FILE_NAME = '知识星球_编程碎碎念.pdf'  # 生成PDF文件的名字
    DOWLOAD_PICS = False  # 是否下载图片 True | False 下载会导致程序变慢
    DOWLOAD_COMMENTS = True  # 是否下载评论
    ONLY_DIGESTS = False  # True-只精华 | False-全部
    FROM_DATE_TO_DATE = False  # 按时间区间下载
    EARLY_DATE = '2019-10-19T00:00:00.000+0800'  # 最早时间 当FROM_DATE_TO_DATE=True时生效 为空表示不限制 形如'2017-05-25T00:00:00.000+0800'
    LATE_DATE = ''  # 最晚时间 当FROM_DATE_TO_DATE=True时生效 为空表示不限制 形如'2017-05-25T00:00:00.000+0800'
    DELETE_PICS_WHEN_DONE = True  # 运行完毕后是否删除下载的图片
    DELETE_HTML_WHEN_DONE = True  # 运行完毕后是否删除生成的HTML
    COUNTS_PER_TIME = 30  # 每次请求加载几个主题 最大可设置为30
    DEBUG = False  # DEBUG开关
    DEBUG_NUM = 120  # DEBUG时 跑多少条数据后停止 需与COUNTS_PER_TIME结合考虑

    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
    </head>
    <body>
    <h1>{title}</h1>
    <br>{author} - {cretime}<br>
    <p>{text}</p>
    </body>
    </html>
    """
