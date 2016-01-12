# -*- coding: utf-8 -*-
{
    'name': 'voucher',
    'version': '0.1',
    'author': 'Lâm Gia Huy',
    'category': '',
    'website': '',
    'summary': '',
    'description':  """
Module này bổ sung cho module campaign vê mục coupon
===================================================
""",     
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