{
    'name' : 'Module custom purchase',
    'version' : '17.0',
    'category' : 'purchase',
    'summary' : 'Purchase Custom Module',
    'description' : """ 
        Purcase custom module uji  
    """,
    'website' : '',
    'author' : 'arie@uniteksolusi.com',
    'depends'  : ['web','base'],
    'data' : [
            'security/ir.model.access.csv',
            'views/arie_purchase_view.xml',   # Mendefinisikan view tree
            'views/arie_purchase_action.xml', # Menggunakan view tree
            'views/arie_purchase_menuitem.xml',
        ],
    'installable' : True,
    'license' : 'OEEL-1',
      
}