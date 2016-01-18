from openerp.osv import fields, osv
import datetime
from datetime import datetime
import time
import random, string
from mako.runtime import _inherit_from



class marketing_campaign(osv.osv):   
    _inherit = "marketing.campaign"      
    _columns = {        
        'code_compaign': fields.char('Compaign Code'),      
        'start_day': fields.date('Start Time'),
        'end_day': fields.date('End Time'),       
        'shop': fields.char('Shop', size=512),       
        } 
    
    def show_voucher(self, cr, uid, vals,context=None):
        rec = self.browse(cr, uid, vals[0], context)
        obj_voucher= self.pool.get('voucher')
        list_voucher= obj_voucher.browse(cr, uid, rec, context=context)
        print"--------------"
        return 