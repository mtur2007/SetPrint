
import numpy as np
from pynput import keyboard

'''
=============================================================================================================================================================
・初歩的な整列
'''

#数値の int部分を見た目的に表示させる様にする自作関数
def Myint(num):
    num = str(num)
    for line in range(len(num)):
        if num[line] == ".":
            return int(num[:line])
    return int(num)

def access_nested_list(nested_list,indices):
    
    for i,index in enumerate(indices):
        
        if (0 <= index < len(nested_list)):             
            # int または str の場合、最後のインデックスでない場合はNoneを返す
            if not isinstance(nested_list[index], (list, np.ndarray)):
                if i == len(indices) - 1:
                    value = nested_list[index]
                    return '\033[1;32m'+str(value).replace('\n', '').replace(', ', ',')+'\033[30m : \033[1;34m'+ type(value).__name__ +'\033[0m'
                else:
                    return '\033[31mNone\033[0m'  # インデックスが範囲外の場合はNoneを返す
                
            nested_list = nested_list[index]

        else:
            return '\033[31mNone\033[0m'  # インデックスが範囲外の場合はNoneを返す
    
    
    # 最終的な要素がリストまたは配列の場合
    else:
        value = nested_list
        return '\033[1;32m'+str(value).replace('\n', '').replace(' ', '')+'\033[30m : \033[1;34m'+ type(value).__name__ +'\033[0m'

#------------------------------------------------------------------------------------------------------------------------------------------------------------

#リストに格納されている情報を文字とみて整列させる関数(main)
def set_txt(txtslist,mode,position):

    if mode == 0:
        Max = 0
        len_list = []

        for line in txtslist:
            len_list.append(len(line))
            if len(line) > Max:
                Max = len(line)

        New_list = []
        Line_list = []
        for nouse in range(Max):
            New_list.append("")

        for line in txtslist:
            Set_list = New_list[:]

            for number in range(len(line)):
                Set_list[number] = line[number]
            
            Line_list.append(Set_list)
        
        Line_list = np.array(Line_list)

        search_list = []
        for num in range(np.shape(Line_list)[1]):
            search_list.append(Line_list[:,num])

        search_list = np.array(set_txt(search_list,1,position))

        Line_list = []
        
        for num in range(np.shape(search_list)[1]):
            Line_list.append(search_list[:,num])
        
        returndata = []

        for line in range (np.shape(Line_list)[0]):
            cut = len_list[line]
            listline = Line_list[line].tolist()
            returndata.append(listline[:cut])

        return returndata

    
    elif mode == 1:

        for line in range(len(txtslist)):
            Maxtxtlen = 0

            for num in txtslist[line]:

                if len(str(num)) > Maxtxtlen:
                    Maxtxtlen = len(str(num))

            Maxlen = Maxtxtlen

            for nowread in range(len(txtslist[line])):
                txt = txtslist[line][nowread]
                Air = Maxlen - len(str(txt))

                if position == 0:

                    txtslist[line][nowread] = str(txt) + (Air * " ")
                elif position == 1:
                    txtslist[line][nowread] = (Air//2 * " ") + str(txt) + ((Air//2 + Air%2) * " ")
                elif position == 2:
                    txtslist[line][nowread] = (Air * " ") + str(txt)

        return txtslist#[:-1]

#リストに格納されている情報を文字とみて整列させる関数(引数処理)
def set_txts(txtslist,mode,position):

    if isinstance(txtslist[0], list) == False:
        txtslist = [txtslist]
        mode = 1

    if position == "left":
        position = 0
    if position == "center":
        position = 1
    if position == "right":
        position = 2

    txtslist = set_txt(txtslist,mode,position)

    return txtslist

#------------------------------------------------------------------------------------------------------------------------------------------------------------

#リストに格納されている情報を文字とみて数値させる関数(main)
def set_number(numberslist,mode):

    if mode == 0:
        Max = 0
        len_list = []

        for line in numberslist:
            len_list.append(len(line))
            if len(line) > Max:
                Max = len(line)

        New_list = []
        Line_list = []
        for nouse in range(Max):
            New_list.append("")

        for line in numberslist:
            Set_list = New_list[:]

            for number in range(len(line)):
                Set_list[number] = line[number]
            
            Line_list.append(Set_list)
        
        Line_list = np.array(Line_list)

        search_list = []
        for num in range(np.shape(Line_list)[1]):
            search_list.append(Line_list[:,num])

        search_list = np.array(set_number(search_list,1))

        Line_list = []
        
        for num in range(np.shape(search_list)[1]):
            Line_list.append(search_list[:,num])
        
        returndata = []

        for line in range (np.shape(Line_list)[0]):
            cut = len_list[line]
            listline = Line_list[line].tolist()
            returndata.append(listline[:cut])

        return returndata

    
    elif mode == 1:

        for line in range(len(numberslist)):
            Maxintlen,Maxfloatlen = 0,0

            for num in numberslist[line]:

                if len(str(Myint(num))) > Maxintlen:
                    Maxintlen = len(str(Myint(num)))

                if len(str(num)) - len(str(Myint(num))) > Maxfloatlen:
                    Maxfloatlen = len(str(num)) - len(str(Myint(num)))

            Maxlen = Maxintlen + Maxfloatlen
            
            for nowread in range(len(numberslist[line])):
                num = numberslist[line][nowread]
                Air0 = Maxintlen - len(str(Myint(num)))
                Air1 = Maxlen - (Air0 + len(str(num)))

                numberslist[line][nowread] = (Air0 * " ") + str(num) + (Air1 * " ")

        return numberslist#[:-1]

#リストに格納されている情報を数値とみて整列させる関数(引数処理)
def set_numbers(numberslist,mode):

    if isinstance(numberslist[0], list) == False:
        numberslist = [numberslist]
        mode = 1
    
    numberslist = set_number(numberslist,mode)

    return numberslist

'''
=============================================================================================================================================================
ブロック状の配列にボーダーをつけ見やすくする関数。
'''

#1次元配列毎の2次元配列部分を1列ごとに整列させる関数
def slice_blocks(datas,mode):

    if isinstance(datas[0][0], list) == False:
        datas = [datas]
        mode = 1

    Allprint_txt = []
    Lineslist = []

    #リストの２次元配列ごとに, 3次元配列同士の要素を縦方向毎になる様に入れ変える
    for line in datas:
        # [[],[],[]]
        #  ^  ^  ^
        max= 0
        for data in line:
            # [ [ [],[] ], [ [],[] ] ,[ [],[] ] ]
            #      ^  ^       ^  ^       ^  ^

            if len(data) > max:
                max = len(data)

        printline = []
        for nouse in range(max):
            printline.append([])
        for data in line:
            if len(data) == 0:
                data.append("")
            for dataline in range(len(data)):
                printline[dataline].append(data[dataline])

            for num in range((max-1 - dataline)):
                printline[dataline + num+1].append('')

        for line in printline:
            Allprint_txt.append(line)
        
        Lineslist.append(len(Allprint_txt)-1)
    
    set_datas = set_txts(Allprint_txt,mode,0)

    set_shape = []
    start = 0
    finish = Lineslist[0] + 1
    set_shape.append(set_datas[start:finish])


    for linenum in range(len(Lineslist)-1):
        linenum += 1

        start = Lineslist[linenum-1] + 1
        finish = Lineslist[linenum] + 1
        set_shape.append(set_datas[start:finish])

    return set_shape

'''
=============================================================================================================================================================
リストを整列させるクラス。
'''

class setprint:

    def __init__(self, input_list):
        self.input_list = input_list

    '''
    =============================================================================================================================================================
    ブロック状の配列にボーダーをつけ見やすくする関数。
    '''

    def blocks_border_print(self, **kwargs):
        key_list = ['All_blocks','line_title','guide']
        diff_key = list(kwargs.keys())
        for key in key_list:
            if key in kwargs:
                diff_key.remove(key)
        
        if len(diff_key) > 0:
            print(str(diff_key) + '存在しないキーです。')
            return KeyError
        
        if 'All_blocks' in kwargs:
            All_blocks = kwargs['All_blocks']
        else:
            All_blocks = self.input_list
        
        if 'line_title' in kwargs:
            line_title = kwargs['line_title']

        if 'guide' in kwargs:
            guide = kwargs['guide']
        else:
            guide = False

        slice_data = slice_blocks(All_blocks,0)
        printlist = []
        linelen0 = 0

        if guide == True:
            max_leny = 0
            for line in line_title:
                if max_leny < len(str(line)):
                    max_leny = len(str(line))
            max_leny += 2
            sample_guide = f" {max_leny * ' '} |  "
        else:
            sample_guide = "|  "

        list_index = []
        for linenum in range(len(slice_data)):
            dataline = slice_data[linenum]
            if len(dataline) != 0:
                writeline = []

                #それぞれのラインに横枠をつける
                list_index.append(dataline[0])
                for linenum in range(len(dataline)-1):
                    line = dataline[linenum+1]
                    printline = sample_guide
                    for txt in line:
                        printline +=  txt + "  |  "
                    printline = printline[:-2]

                    writeline.append(printline)

                
                linelen1 = len(printline)

                #横枠の作成...表示文字列列の以前の長さと現在の長さによって長さの基準を変える
                if linelen0 > linelen1:
                    printlist.append(f"{'='*linelen0}\n")
                    printlist.append('\n')
                else:
                    printlist.append(f"{'='*linelen1}\n")
                    printlist.append('\n')

                linelen0 = linelen1

                for line in writeline:
                    printlist.append(f"{line}\n")

                printlist.append('\n') #※0
            
            else:
                printlist.append(f"{'='*linelen0}\n")
                printlist.append('\n')
                if linenum != len(slice_data)-1:
                    printlist.append(f" >> Xx__No_data__xX\n")
                    printlist.append('\n')
                else:
                    printlist.append(f" >> Xx__No_data__xX\n")
                linelen0 = 0

        if len(slice_data[-1]) != 0:
            printlist.append(f"{'='*linelen1}\n")

        #print(f'[SET_border, border] time: {finish - start}')

        #ガイド(index)を追加する場合の処理
        if guide == True:

            read = 0

            sample_guide = f" {max_leny * ' '} "
            set_index = 1
            for linenum in range(len(slice_data)):
                line = slice_data[linenum]
                indexline = list_index[linenum]

                if len(line) != 0:
                    if len(line_title)-1 >= linenum: 
                        txt = '{' + str(line_title[linenum]) + '}'
                    else:
                        txt = '{}'

                    air = (max_leny - len(txt)) * ' '
                    guidex0 = ' ' + air + str(txt) + ' |  '
                    
                    guidex1 = sample_guide + '|--'
                    guidex2 = sample_guide + ':  '

                    for txtnum in range(len(line[0])):
                        txt_index = indexline[txtnum]

                        guidex0 += str(txt_index) + "  |  "
                        guidex1 += len(line[0][txtnum]) * "-" + "--|--"
                        guidex2 += len(line[0][txtnum]) * " " + "  :  "

                    printlist.insert(set_index,guidex0[:-2]+'\n')
                    printlist.insert(set_index+1,guidex1[:-2]+'\n')

                    #ボーダー作成時に追加した空白部分(※0)はガイドをつける場合、いらないので情報を書き換える。
                    printlist[set_index+2] = guidex2[:-2] + '\n'

                    set_index += len(line)+2 + 2

                else: #データがない時は1文で表示される為、例外処理
                    set_index += 1 +3

            #print(f'[SET_border, guide ] time: {finish - start}')

        return printlist

    '''
    =============================================================================================================================================================
    ・リストの中身やインデックスを調査し、整列させる関数。
    '''

    #リストのインデックスを再帰関数を使って調べていき、指定条件に沿った形で整列し、出力する。12
    def search_index(self, datas):

        self.now_deep += 1 #deepはインデックスの次元測定

        txt_index = ''
        for i in self.now_index:
            txt_index += '['+str(i)+']'
        txt_index += '{n}' 
        txtline = [txt_index]
        insert_index = len(self.Xline_blocks)-1

        if self.keep_start == self.now_deep:

            # < self.MAX_indexlen > インデックス別整列をする為、linenumの値[リストのインデックス]は使わず、リストの一列毎の階層だげを調べる。
            txtline = []

            self.MAX_index = []
            self.MAX_indexlen = []
            self.finish_index = {}

            self.now_index.append('')
            self.Xline_blocks.append('')
            self.keep_txts_data.append('')

            insert_index = len(self.Xline_blocks)-1

            for linenum in range(len(datas)):
                self.keep_index = []
                #now_index[1:]を表す
                line = datas[linenum]
                
                self.now_index[-1] = linenum

                datatype = type(line)

                if datatype == list or datatype == np.ndarray:
                    self.keep_linetxts = []

                    if (self.keep_index in self.MAX_index) == False:
                        self.MAX_index.append(self.keep_index.copy())
                        self.MAX_indexlen.append(5)
                    else:
                        if self.MAX_indexlen[self.MAX_index.index(self.keep_index)] < 5:
                            self.MAX_indexlen[self.MAX_index.index(self.keep_index)] = 5

                    self.keep_linetxts.append([self.keep_index,self.list_txt_image])

                    '''
                    ここに '[' を入れるプログラムを作成する。
                    '''
                    self.search_index(line)
         
                    txtline.append(self.keep_linetxts)
                else:
                    #リストの最下層の場合の処理
                    txt_line = str(line)

                    if (self.keep_index in self.MAX_index) == False:
                        self.MAX_index.append(self.keep_index.copy())
                        self.MAX_indexlen.append(len(txt_line))
                    else:
                        if self.MAX_indexlen[self.MAX_index.index(self.keep_index)] < len(txt_line):
                            self.MAX_indexlen[self.MAX_index.index(self.keep_index)] = len(txt_line)

                    txtline.append([[self.keep_index,txt_line]])
            
           
            if len(datas) >= 1:

                sort_MAX_index = sorted(self.MAX_index)
                sort_MAX_indexlen = []
                for indexline in sort_MAX_index:
                    a = self.MAX_index.index(indexline)
                    sort_MAX_indexlen.append(self.MAX_indexlen[a])
                self.MAX_index,self.MAX_indexlen = sort_MAX_index,sort_MAX_indexlen

                linenum = 0
                self.keep_linetxts = [txt_index] #ガイド

                S_onlylist_index = set()
                F_onlylist_index = set()

                for keep_linenum in range(len(txtline)):
                    keep_line = txtline[keep_linenum]
                    txt = ''
                    #a = 0
                    linenum = 0
                    for keep_txtnum in range(len(keep_line)):
                        keep_txts = keep_line[keep_txtnum]
                        index_line = self.MAX_index[linenum]
                        noput_point = []

                        if keep_txts[0] == index_line:
                            index_len = self.MAX_indexlen[linenum]
                            air = (index_len - len(keep_txts[1])) * ' '
                            txt += air + str(keep_txts[1]) + ' '

                        else:
                            if keep_txts[0] == 'finish':
                                search_finish = keep_txts[1][:-1]
                                search_finish.append(self.finish_index[str(search_finish)])
                            else:
                                search_finish = keep_txts[0]

                            while True:
                                if search_finish == self.MAX_index[linenum]:
                                    if  keep_txts[0] == 'finish':
                                        txt += '] '
                                    else:
                                        air = (self.MAX_indexlen[linenum] - len(keep_txts[1])) * ' '
                                        txt += air + str(keep_txts[1]) + ' '
                                    break
                                else:
                                    if self.MAX_index[linenum][-1] == -1:
                                        
                                        S_onlylist_index.add(len(txt))

                                        key_index = self.MAX_index[linenum][:-1]
                                        key_index.append(self.finish_index[str(key_index)])
                                        noput_point.append(self.MAX_index.index(key_index))
                                        txt += (self.MAX_indexlen[linenum] * ' ') + ' '
                                    else:
                                        if (linenum in noput_point) != True:
                                            txt += (self.MAX_indexlen[linenum] * '-') + ' '
                                        else:
                                            F_onlylist_index.add(len(txt))

                                            del noput_point[noput_point.index(linenum)]
                                            txt += (self.MAX_indexlen[linenum] * ' ') + ' '
                            
                                linenum += 1
                        linenum += 1

                    for i in range(len(self.MAX_index) - linenum):
                        i_index = self.MAX_index[linenum + i]
            
                        if i_index[-1] == -1:
                            
                            S_onlylist_index.add(len(txt))

                            key_index = i_index[:-1]
                            key_index.append(self.finish_index[str(key_index)])
                            noput_point.append(self.MAX_index.index(key_index))
                            txt += (self.MAX_indexlen[linenum + i] * ' ') + ' '
                        else:
                            if ((linenum + i) in noput_point) != True:
                                txt += (self.MAX_indexlen[linenum + i] * '-') + ' '
                            else:

                                F_onlylist_index.add(len(txt))

                                del noput_point[noput_point.index(linenum + i)]
                                txt += (self.MAX_indexlen[linenum + i] * ' ') + ' '

                    self.keep_linetxts.append(txt)

                for linenum in range(len(self.keep_linetxts)-1):
                    linenum += 1
                    for S_index in S_onlylist_index:
                        line = self.keep_linetxts[linenum]

                        if line[S_index] == '[':
                            self.keep_linetxts[linenum] = line[:S_index] + '{' + line[S_index+1:]

                    for F_index in F_onlylist_index:
                        line = self.keep_linetxts[linenum]

                        if line[F_index] == ']':
                            self.keep_linetxts[linenum] = line[:F_index] + ')' + line[F_index+1:]
                    
            #中身のリスト作成
            self.Xline_blocks[insert_index] = self.keep_linetxts

            txt_keep_index = self.now_index.copy()
            txt_keep_index[-1] = 'n'

            total = self.MAX_indexlen[0] + 1
            x_lens = [0]
            for datanum in range(len(self.MAX_indexlen)-1):
                x_lens.append(total)
                total += self.MAX_indexlen[datanum+1] + 1

            del_MAXindex = self.MAX_index.copy()
            for linenum in range(len(self.MAX_index)-1):
                line = self.MAX_index[linenum+1]
                if line[-1] == -1:
                    del_index = del_MAXindex.index(line)
                    del del_MAXindex[del_index]
                    del self.MAX_indexlen[del_index]
                    del x_lens[del_index]

                    search_line = line[:-1]
                    search_line.append(self.finish_index[str(search_line)])
                    del_index = del_MAXindex.index(search_line)
                    del del_MAXindex[del_index]
                    del self.MAX_indexlen[del_index]
                    del x_lens[del_index]

            self.keep_txts_data[insert_index] = [txt_keep_index,del_MAXindex,self.MAX_indexlen,x_lens]       

        elif self.keep_start < self.now_deep <= self.keep_finish:

            self.keep_index.append(-1)
            self.now_index.append('')
            
            insert_index = self.keep_index.copy()
            if (insert_index in self.MAX_index) == False:
                self.MAX_index.append(insert_index)
                self.MAX_indexlen.append(1)
            else:
                if self.MAX_indexlen[self.MAX_index.index(insert_index)] < 1:
                    self.MAX_indexlen[self.MAX_index.index(insert_index)] = 1

            self.keep_linetxts.append([insert_index,'['])


            for linenum in range(len(datas)):

                line = datas[linenum]

                self.keep_index[-1] = linenum
                self.now_index[-1] = linenum

                datatype = type(line)
                if datatype == list or datatype == np.ndarray:
                    insert_index = self.keep_index.copy()
                    if (insert_index in self.MAX_index) == False:
                        self.MAX_index.append(insert_index)
                        self.MAX_indexlen.append(5)
                    else:
                        if self.MAX_indexlen[self.MAX_index.index(insert_index)] < 5:
                            self.MAX_indexlen[self.MAX_index.index(insert_index)] = 5

                    self.keep_linetxts.append([insert_index,self.list_txt_image])

                    '''
                    ここに '[' を入れるプログラムを作成する。
                    '''
                    self.search_index(line) 
                else:
                    txt_line = str(line)
                    #テキストの場合、中身の長さを入れ
                    
                    insert_index = self.keep_index.copy()

                    if (insert_index in self.MAX_index) == False:
                        self.MAX_index.append(insert_index)
                        self.MAX_indexlen.append(len(txt_line))
                    else:
                        if self.MAX_indexlen[self.MAX_index.index(insert_index)] < len(txt_line):
                            self.MAX_indexlen[self.MAX_index.index(insert_index)] = len(txt_line)

                    self.keep_linetxts.append([insert_index,txt_line])
            
            insert_index = self.keep_index.copy()
            insert_index[-1] += 1

            if (insert_index in self.MAX_index) == False:
                self.MAX_index.append(insert_index)
                self.MAX_indexlen.append(1)
            else:
                if self.MAX_indexlen[self.MAX_index.index(insert_index)] < 1:
                    self.MAX_indexlen[self.MAX_index.index(insert_index)] = 1

            self.keep_linetxts.append(['finish',insert_index,'finish'])

            key = str(insert_index[:-1])
            if (key in self.finish_index) == False:
                self.finish_index[key] = insert_index[-1]
            else:
                if self.finish_index[key] < insert_index[-1]:
                    self.finish_index[key] = insert_index[-1]

            '''
            ここに ']' を 入れるプログラムを作成する。
            '''

            del self.keep_index[-1]
        
        else:
            self.Xline_blocks.append('')
            insert_index = len(self.Xline_blocks)-1

            self.now_index.append('')

            max_indexlen = 0
            self.keep_txts_data.append('')

            for linenum in range(len(datas)):
                line = datas[linenum]

                self.now_index[-1] = linenum

                txt = ""
                for i in self.now_index:
                    txt += "[" + str(i) + "]"
                datatype = type(line)
                if datatype == list or datatype == np.ndarray:
                    self.search_index(line)

                    txtline.append(f'data_type: {datatype}')
                else:
                    txtline.append(str(line))
                    #リストの最下層の場合の処理
                
                if len(txtline[linenum+1]) > max_indexlen:
                    max_indexlen = len(txtline[linenum+1])
                
                
            #中身のリスト作成
            self.Xline_blocks[insert_index] = txtline
            txt_keep_index = self.now_index.copy()
            txt_keep_index[-1] = 'n'
            self.keep_txts_data[insert_index] = [txt_keep_index,max_indexlen]

        del self.now_index[-1] #インデックスの調査が終わったら戻す
        self.now_deep -= 1

    #リストを整列する際の条件を整理したり、１次元毎にブロックを一段ずらす為、１次元までこの関数で処理し、以降は search_index で調査。
    def set_list(self, guide,keep_start,keeplen):
        
        datas = self.input_list

        self.keep_start = keep_start
        if self.keep_start == False:
            self.keep_start = 0
            self.keep_finish = 0
        else:
            
            self.keep_finish = self.keep_start + keeplen

        self.now_deep = 1 #now_deepはインデックスの次元測定
        self.now_index = []
        self.Xline_blocks = []
        self.keep_txts_data = []
        self.keep_index = []

        txtline = ['{n}']
        All_blocks = []
        keep_Ylines_data = []

        self.list_txt_image = '►list'

        if self.keep_start == self.now_deep:

            # < self.MAX_indexlen > インデックス別整列をする為、linenumの値[リストのインデックス]は使わず、リストの一列毎の階層だげを調べる。
            txtline = []
            self.MAX_index = []
            self.MAX_indexlen = []
            self.finish_index = {}

            self.now_index.append('')

            self.Xline_blocks.append('')
            insert_index = len(self.Xline_blocks)-1
            self.keep_txts_data.append('')
            keep_Ylines_data.append('')

            for linenum in range(len(datas)):
                self.keep_index = []
                copy_keep_index = self.keep_index.copy()
                line = datas[linenum]
                
                self.now_index[-1] = linenum

                datatype = type(line)

                if datatype == list or datatype == np.ndarray:
                    self.keep_linetxts = []
                    
                    if (copy_keep_index in self.MAX_index) == False:
                        self.MAX_index.append(copy_keep_index)
                        self.MAX_indexlen.append(5)
                    else:
                        if self.MAX_indexlen[self.MAX_index.index(copy_keep_index)] < 5:
                            self.MAX_indexlen[self.MAX_index.index(copy_keep_index)] = 5

                    self.keep_linetxts.append([copy_keep_index,self.list_txt_image])
                    '''
                    ここに '[' を入れるプログラムを作成する。
                    '''
                    self.search_index(line)
            
                    txtline.append(self.keep_linetxts)
                else:
                    #txtline.append(str(line))
                    #リストの最下層の場合の処理
                    txt_line = str(line)

                    if (copy_keep_index in self.MAX_index) == False:
                        self.MAX_index.append(copy_keep_index)
                        self.MAX_indexlen.append(len(txt_line))
                            #print(self.MAX_indexlen)
                    else:
                        if self.MAX_indexlen[self.MAX_index.index(copy_keep_index)] < len(txt_line):
                            self.MAX_indexlen[self.MAX_index.index(copy_keep_index)] = len(txt_line)

                    txtline.append([[copy_keep_index,txt_line]])
                
            
            #print('\n'+('-'*84)+'\n'+txt_index)
            
            if len(datas) >= 1:
        
                sort_MAX_index = sorted(self.MAX_index)
                sort_MAX_indexlen = []
                for line in sort_MAX_index:
                    a = self.MAX_index.index(line)
                    sort_MAX_indexlen.append(self.MAX_indexlen[a])
                self.MAX_index,self.MAX_indexlen = sort_MAX_index,sort_MAX_indexlen

                linenum = 0
                self.keep_linetxts = ['[]'] #ガイド

                S_onlylist_index = set()
                F_onlylist_index = set()

                for keep_linenum in range(len(txtline)):
                    keep_line = txtline[keep_linenum]
                    txt = ''

                    linenum = 0
                    for keep_txtnum in range(len(keep_line)):
                        keep_txts = keep_line[keep_txtnum]
                        index_line = self.MAX_index[linenum]
                        noput_point = []

                        if keep_txts[0] == index_line:
                            index_len = self.MAX_indexlen[linenum]
                            air = (index_len - len(keep_txts[1])) * ' '
                            txt += air + str(keep_txts[1]) + ' '

                        else:
                            if keep_txts[0] == 'finish':
                                search_finish = keep_txts[1][:-1]
                                search_finish.append(self.finish_index[str(search_finish)])
                            else:
                                search_finish = keep_txts[0]

                            while True:
                                if search_finish == self.MAX_index[linenum]:
                                    if  keep_txts[0] == 'finish':
                                        txt += '] '
                                    else:
                                        air = (self.MAX_indexlen[linenum] - len(keep_txts[1])) * ' '
                                        txt += air + str(keep_txts[1]) + ' '
                                    break
                                else:
                                    if self.MAX_index[linenum][-1] == -1:
                                        
                                        S_onlylist_index.add(len(txt))

                                        a = self.MAX_index[linenum][:-1]
                                        a.append(self.finish_index[str(self.MAX_index[linenum][:-1])])
                                        noput_point.append(self.MAX_index.index(a))
                                        txt += (self.MAX_indexlen[linenum] * ' ') + ' '
                                    else:
                                        if (linenum in noput_point) != True:
                                            txt += (self.MAX_indexlen[linenum] * '-') + ' '
                                        else:

                                            F_onlylist_index.add(len(txt))

                                            del noput_point[noput_point.index(linenum)]
                                            txt += (self.MAX_indexlen[linenum] * ' ') + ' '

                                linenum += 1
                        linenum += 1
                
                    for i in range(len(self.MAX_index) - linenum):
                        i_index = self.MAX_index[linenum + i]
            
                        if i_index[-1] == -1:
                            
                            S_onlylist_index.add(len(txt))

                            key_index = i_index[:-1]
                            key_index.append(self.finish_index[str(key_index)])
                            noput_point.append(self.MAX_index.index(key_index))
                            txt += (self.MAX_indexlen[linenum + i] * ' ') + ' '
                        else:
                            if ((linenum + i) in noput_point) != True:
                                txt += (self.MAX_indexlen[linenum + i] * '-') + ' '
                            else:

                                F_onlylist_index.add(len(txt))

                                del noput_point[noput_point.index(linenum + i)]
                                txt += (self.MAX_indexlen[linenum + i] * ' ') + ' '
                                
                    self.keep_linetxts.append(txt)
            
                for linenum in range(len(self.keep_linetxts)-1):
                    linenum += 1
                    for S_index in S_onlylist_index:
                        line = self.keep_linetxts[linenum]

                        if line[S_index] == '[':
                            self.keep_linetxts[linenum] = line[:S_index] + '{' + line[S_index+1:]

                    for F_index in F_onlylist_index:
                        line = self.keep_linetxts[linenum]

                        if line[F_index] == ']':
                            self.keep_linetxts[linenum] = line[:F_index] + ')' + line[F_index+1:]

                    
            #中身のリスト作成
            self.Xline_blocks[insert_index] = self.keep_linetxts
            All_blocks = [self.Xline_blocks]

            txt_keep_index = self.now_index.copy()
            txt_keep_index[-1] = 'n'


            total = self.MAX_indexlen[0] + 1
            x_lens = [0]
            for datanum in range(len(self.MAX_indexlen)-1):
                x_lens.append(total)
                total += self.MAX_indexlen[datanum+1] + 1

            del_MAXindex = self.MAX_index.copy()
            for linenum in range(len(self.MAX_index)-1):
                line = self.MAX_index[linenum+1]
                if line[-1] == -1:
                    del_index = del_MAXindex.index(line)
                    del del_MAXindex[del_index]
                    del self.MAX_indexlen[del_index]
                    del x_lens[del_index]
                    search_line = line[:-1]
                    search_line.append(self.finish_index[str(search_line)])
                    del_index = del_MAXindex.index(search_line)
                    del del_MAXindex[del_index]
                    del self.MAX_indexlen[del_index]
                    del x_lens[del_index]

            self.keep_txts_data[insert_index] = [txt_keep_index,del_MAXindex,self.MAX_indexlen,x_lens]
            keep_Ylines_data = [self.keep_txts_data]

            line_title = ['']
            

        else:
            line_title = ['']
            max_indexlen = 0

            for linenum in range(len(datas)):
                self.Xline_blocks = []
                self.keep_txts_data = []
                line = datas[linenum]
                self.now_index = [linenum]

                datatype = type(line)
                if  datatype == list or datatype == np.ndarray:
                    self.search_index(line)
                    All_blocks.append(self.Xline_blocks)
                    keep_Ylines_data.append(self.keep_txts_data)

                    txtline.append(f'data_type: {datatype}')
                    line_title.append(linenum)

                else:
                    txtline.append(str(line))
                    #リストの最下層の場合の処理
                    All_blocks.append([[f'[{str(linenum)}]{{n}}','index_Err']])
                    keep_Ylines_data.append([[[linenum,0],9]])

                    line_title.append(linenum)
                if len(txtline[linenum+1]) > max_indexlen:
                    max_indexlen = len(txtline[linenum+1])


            txtline = [txtline]

            txt_keep_index = self.now_index.copy()
            txt_keep_index[-1] = 'n'
            keep_Ylines_data.insert(0,[[txt_keep_index,max_indexlen]])

            All_blocks.insert(0,txtline)
        
        
        #データを縦方向に合わせて整列し、結果をファイルに書き込む。
        self.All_blocks = All_blocks
        set_border_list = self.blocks_border_print(All_blocks = All_blocks, line_title = line_title, guide = guide)

        set_data_dict = {

        "input_list" : datas,
        "grid_slice" : set_border_list,
        'grid_block' : All_blocks,

        'block_keep_data' : keep_Ylines_data

        }

        self.set_data_dict = set_data_dict

        return set_data_dict

    '''
    =============================================================================================================================================================
    set_listで大まかなガイドが表示されるが、さらに詳しい格納情報を見ることが出来るようにする関数。
    '''
    def Block_GuidePrint(self, y,x,gx,gy):

        self.y = abs(self.y % len(self.block_keep_data))
        self.x = abs(self.x % len(self.block_keep_data[self.y]))

        y,x = self.y,self.x
        k_data = self.block_keep_data[y][x]
   
        if len(k_data) == 4:
            y_lens = len(self.block[y][x])-1
            class_index = k_data[0][:-1]
            indexs = k_data[1]
            x_lens = k_data[2]
            positions = k_data[3]
        elif len(k_data) == 2:
            y_lens = len(self.block[y][x])-1
            class_index = k_data[0][:-1]
            indexs = [[]]
            x_lens = [k_data[1]]
            positions = [0]


        gx = abs(gx%len(positions))
        gy = abs(gy%y_lens)

        guide_index = ''
        for line in class_index:
            guide_index += f'[\033[38;2;127;82;0m{str(line)}\033[0m]'
        
        guide_index += f'{{\033[38;2;255;165;0m\033[1m{str(gy)}\033[0m}}'
        for line in indexs[gx]:
            guide_index += f'[\033[1;34m{str(line)}\033[0m]'

        this = class_index+[gy]+indexs[gx]
        value = access_nested_list(self.input_list,this)

        # 行1を更新
        print("\033[F\033[F\033[Kindex \\ " + guide_index)
        # 行2を更新
        if len(value) >= 195:
            print(' value \\ \033[K'+value[:150]+'\033[0m')
        else:
            print(' value \\ \033[K'+value)

        guide = ' '
        for line in range(gx):
            guide += (positions[line]+1 - len(guide)) * ' '
            line = x_lens[line]
            guide += (line//2) * ' ' + '>'
        
        guide += (positions[gx]+1 - len(guide)) * ' '+ (x_lens[gx]//2)*' ' + ' ▼' + guide_index
        data = self.block[y][x]
        write_txt = []

        start = positions[gx]
        finish = start + x_lens[gx]
        for linenum in range(len(data)-1):
            line = data[linenum+1]
            write_txt.append(' ' + line[:start] +' '+ line[start:finish] +' '+ line[finish:])

        guide_line = '━' * len(write_txt[0])
        write_txt.insert(gy,guide_line)
        write_txt.insert(gy+2,guide_line)


        line = write_txt[gy]
        write_txt[gy] = line[:start] +' ┏'+ x_lens[gx]*' ' +'┓ '+ line[finish+4:]

        line = write_txt[gy+1]
        write_txt[gy+1] = line[:start] +'  '+ line[start+2:finish+2] + '  ' + line[finish+4:]

        line = write_txt[gy+2]
        write_txt[gy+2] =  line[:start] +' ┗'+ x_lens[gx]*' ' +'┛ '+ line[finish+4:]


        with open(self.output_path ,'w') as f:
            
            f.write('{guide}' + guide + '\n\n')
            for line in write_txt:
                f.write('       ' + line + '\n')

            f.write('\n')
            for line in self.block_keep_data[y][x]:
                f.write(str(line) + '\n')

    def on_press(self, key):
        try:
            
            key = key.char


            if key == 'a':
                self.gx -= 1
            elif key == 'd':
                self.gx += 1
            elif key == 'w':
                self.gy -= 1
            elif key == 's':
                self.gy += 1

            elif key == 'f':
                self.x -= 1
            elif key == 'h':
                self.x += 1
            elif key == 't':
                self.y -= 1
            elif key == 'g':
                self.y += 1

            self.Block_GuidePrint(self.y,self.x,self.gx,self.gy)


        except AttributeError:
            if key == keyboard.Key.esc:
                # ESC キーが押された場合に終了
                return False

    def pick_guidePrint(self, output_path):

        # リスト内包表記を使って、キーに対応する値を取り出す
        try:
            set_data_dict = self.set_data_dict
        except:
            print('`pick_guidePrint`関数を実行するには "set_list"関数 を先に実行してください。')
            return
        
        self.input_list      = set_data_dict['input_list']
        self.block           = set_data_dict['grid_block']
        self.block_keep_data = set_data_dict['block_keep_data']

        self.output_path = output_path

        self.y,self.x = 0,0
        self.gy,self.gx = 0,0

        print()
        print('連動先のファイル : '+self.output_path)
        print()
        print()
        print()
        self.Block_GuidePrint(self.y,self.x,self.gx,self.gy)
        #キーボードのリスナーを開始
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
 