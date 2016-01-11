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
        } 
    
    def show_voucher(self, cr, uid, vals,context=None):
        rec = self.browse(cr, uid, vals[0], context)
        obj_voucher= self.pool.get('voucher')
        list_voucher= obj_voucher.browse(cr, uid, rec, context=context)
        print"--------------"
        return 