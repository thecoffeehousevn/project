from openerp.osv import fields, osv
import datetime
from datetime import datetime
import time
import random, string
from openerp import _
from openerp.exceptions import Warning
import xlwt

class Voucher(osv.osv):
    _name = "voucher"
    _description = "xemtaomavoucher"
    _columns = {        
        'name': fields.char('Coupon Code', size=512, required=True),
        'campagin': fields.many2one('marketing.campaign', 'Campagin', required=True),      
        'quantum': fields.integer('Quantity'),
        'code_size': fields.integer('Length'),
        'status': fields.boolean('Used', required=True),
        'alphabet': fields.integer('Alphabet'),
        'stand': fields.integer('Stand'),        

         
        } 
    def return_file_excell(self):
        book = xlwt.Workbook()
        sh = book.add_sheet("sheet 1")
        book.save("listcoupon")    
    
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
            raise Warning(_("Your code Length can't create this Quantity coupon"))
        elif read_code_campaign['code_compaign']==False:
            raise Warning(_("Your campaign haven't code. We can't create coupon"))
        elif vals['quantum']== False:
            raise Warning(_("You can't set None Quantity. We can't create coupon"))
        elif vals['code_size']== False:
            raise Warning(_("You can't set None Code Length. We can't create coupon"))        
        else:
            list=(range(min,max))
            if vals['alphabet'] != False:
                list=self.convert_alphabet_list(list,vals['stand'],vals['alphabet'])      
            for i in range(0,quantum-1):
               number=random.randrange(len(list))             
               vals = {'name':read_code_campaign['code_compaign']+str(list[number]), 'campagin':vals['campagin'],'status':False}
               super(Voucher,self).create(cr,uid,vals,context=context)
               list.remove(list[number])
            vals = {'name':read_code_campaign['code_compaign']+str(list[1]),'campagin':vals['campagin'],'status':False}
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
            list_used.append (self.add_alphabet(i,quantum_alphabet,stand))
            #   list_alphabet.remove(list_alphabet[number])
        return list_used
    def add_alphabet(self,text,quantum_alphabet,stand):
        test=""
        check_stand=0        
        list_alphabet=['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']          
        list_stand=[]        
        if len(str(stand))>1:
            for i in str(stand):                
                list_stand.append(i)
        
        if len(list_stand)>1 :             
            for i in str(text):
                for y in list_stand:
                    if y == str(check_stand):                        
                            number=random.randrange(len(list_alphabet))                             
                            test=test+list_alphabet[number]                           
                test=test+i
                check_stand=check_stand+1
        else:            
            if(stand>0):
                for i in str(text):               
                    if stand == check_stand:  
                        for j in range(0,quantum_alphabet):                      
                            number=random.randrange(len(list_alphabet))                                
                            test=test+list_alphabet[number]                           
                    test=test+i
                    check_stand=check_stand+1
            else: 
                test=text
        return test
    