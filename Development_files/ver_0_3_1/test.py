from setprint import SetPrint


#                 整形したい配列を指定
#                         ∨
list_data    = SetPrint([0,[],[]])

#            '''  展開したい方向を指定
#                 （詳細はgithubより）  '''
#                         ∨
keep_settings = {1:'x',3:'yf',4:'f'}

# 整形の実行
format_texts  = list_data.set_collection ( route=True, y_axis=False, keep_settings=keep_settings )

# 結果の表示 : テキストファイルへの書き込み 
# (表示方法は任意 : !!! 最後に 改行'\n' を忘れずに !!! )
with open('output.txt','w') as f:
    for line in format_texts:
            f.write(line+'\n')