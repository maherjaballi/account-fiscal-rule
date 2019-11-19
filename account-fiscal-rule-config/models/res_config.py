# -*- coding: utf-8 -*-
import openerp
from openerp import api, fields, models, _

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    module_account_product_fiscal_classification = fields.Boolean(string='Account Product Fiscal Classification',
        help='* Add a new light concept fiscal_classification to associate possible\n'
              'purchase and sale taxes;\n'
             '-This installs the module account_product_fiscal_classification.')
    
    module_account_product_fiscal_classification_test = fields.Boolean(string='Account Product Fiscal Classification Test',
         help=' This module is a technical module to test some features of the module \n' 
              ' ``account_product_fiscal_classification`` (same repository), that requires \n' 
              ' chart Template. \n' 
             '-This installs the module account_product_fiscal_classification_test.')
    