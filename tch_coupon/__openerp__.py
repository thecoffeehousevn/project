# -*- coding: utf-8 -*-
{
    'name': 'tch_coupon',
    'version': '0.2',
    'author': 'Lâm Gia Huy',
    'category': '',
    'website': '',
    'summary': '',
    'description': "Module thêm mục coupon trong menu campaigns của module lead automation chức năng tạo ra coupon",     
     'depends': ['marketing_campaign',                 
    ], 
    'data': [ 
        'voucher.xml',
        'marketing_campaign.xml',
        'menu.xml',
    ],
    'installable': True,
    'application': False,
}