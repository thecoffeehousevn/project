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
    
