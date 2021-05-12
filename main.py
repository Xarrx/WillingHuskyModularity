from src.mparse.mparse import traverse_menu

""" 
Example of menu dictionary structure
"""
def termState1_callback(s):
  print('Callback args: {}'.format(s))
  return

proto = {

  'options' : {
    'logging' : True,
    'title_format' : '~= {} =~',
    'title_ul' : False,
    'title_ul_char' : '=',
    'row_format' : '{} -> {}',
  },

  'init_menu_key' : 'main_menu',
  'main_menu' : {
    'head' : 'Prototype Menu',
    'options' : [
      {
        'desc' : 'Branch to menu 1',
        'flow' : 1,
        'menu_key' : 'branch1'
      },
      {
        'desc' : 'Branch to menu 2',
        'flow' : 2,
        'menu_key' : 'branch2'
      }
    ]
  },

  'branch1' : {
    'head' : 'Branch 1 Menu',
    'options' : [
      {
        'desc' : 'Branch to menu 6',
        'flow' : 1,
        'menu_key' : 'branch6',
        'store' : {
          'var1' : 'value1',
          'var2' : 0
        }
      },
    ]
  },

  'branch2' : {
    'head' : 'Branch 2 Menu',
    'options' : []
  },

  'branch6' : {
    'head' : 'Branch 6 Menu',
    'options' : [
      {
        'desc' : 'Do terminal state 1',
        'flow' : 1,
        'menu_key' : 'termState1',
        'store' : {
          'var1' : 'value2',
          'var2' : 100
        },

      },
    ]
  },

  'termState1' : {
    'head' : 'term_state_1',
    'options' : [],
    'callback' : termState1_callback
  }
  
}

traverse_menu(proto)
