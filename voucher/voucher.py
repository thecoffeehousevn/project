from openerp.osv import fields, osv
import datetime
from datetime import datetime
import time
import random, string
from openerp import _
from openerp.exceptions import Warning

class Voucher(osv.osv):
    _name = "voucher"
    _description = "xemtaomavoucher"
    _columns = {        
        'name': fields.char('Coupon Code', size=512, required=True),
        'campagin': fields.many2one('marketing.campaign', 'Campagin', required=True),
        'shop': fields.char('Shop', size=512, required=True),
        'quantum': fields.integer('Quantumlyti', required=True),
        'code_size': fields.integer('Size', required=True),
        'status': fields.boolean('Used', required=True),
        'alphabet': fields.integer('Alphabet', required=True),
        'stand': fields.integer('Stand', required=True),        
        'create_time':fields.date('Create Time'),   
        } 
    
    def create(self, cr, uid, vals,context=None):
        min=1
        max=1
        code_campaign_obj = self.pool.get('marketing.campaign')
        campagin_id= vals['campagin']
        read_code_campaign = code_campaign_obj.browse(cr, uid, campagin_id)           
        times_voucher= datetime.now()
        print read_code_campaign['code_compaign']

        size=vals['code_size']     
        for i in range(0,size):
            min=min*10
            max=max*10
        min=min/10               
        quantum=vals['quantum'] 
        max_quantum=max-min
        if(max_quantum<quantum):
           raise Warning(_("Your code size can't create this quantum voucher"))
        else:
            list=(range(min,max))
            list=self.convert_alphabet_list(list,vals['stand'],vals['alphabet'])      
            for i in range(0,quantum-1):
               number=random.randrange(len(list))             
               vals = {'name':read_code_campaign['code_compaign']+list[number], 'campagin':vals['campagin'],'shop':vals['shop'],'quantum':quantum,'code_size':vals['code_size'],'status':False,'alphabet':vals['alphabet'],'stand':vals['stand'],'create_time':times_voucher}
               super(Voucher,self).create(cr,uid,vals,context=context)
               list.remove(list[number])
            vals = {'name':read_code_campaign['code_compaign']+list[1],'campagin':vals['campagin'],'shop':vals['shop'],'quantum':quantum,'code_size':vals['code_size'],'status':False,'alphabet':vals['alphabet'],'stand':vals['stand'],'create_time':times_voucher}
            return super(Voucher,self).create(cr,uid,vals,context=context)
    
    def check_number(self,number,size):
        test=""               
        for i in str(number):
            test=test+str(self.converttostr(i))
        
        return test
   
    def convert_alphabet_list(self,list,stand,quantum_alphabet):
        #list_alphabet=['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
        list_used=[]
        for i in list:
            list_alphabet=['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
            #for j in range(0,3):
            number=random.randrange(len(list_alphabet))            
            list_used.append (self.add_alphabet(i,list_alphabet[number],stand))
            #   list_alphabet.remove(list_alphabet[number])
        return list_used
    def add_alphabet(self,number,text,stand):
        test=""
        check_stand=0               
        for i in str(number):
            if (check_stand==stand):
                test=test+text
                check_stand=check_stand+1
            else:
                test=test+i
                check_stand=check_stand+1
        return test
    