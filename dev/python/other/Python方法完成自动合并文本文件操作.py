
    # coding gbk  
 #www.iplaypy.com
      
    import sys,os,msvcrt  
      
    def join(in_filenames, out_filename):  
        out_file = open(out_filename, 'w+')  
          
        err_files = []  
        for file in in_filenames:  
            try:  
                in_file = open(file, 'r')  
                out_file.write(in_file.read())  
                out_file.write('\n\n')  
                in_file.close()  
            except IOError:  
                print 'error joining', file  
                err_files.append(file)  
        out_file.close()  

        print 'joining completed. %d file(s) missed.' % len(err_files)  

        print 'output file:', out_filename  

        if len(err_files) > 0:  
            print 'missed files:'  
            print '--------------------------------'  
            for file in err_files:  
                print file  
            print '--------------------------------'  
      
    if __name__ == '__main__':  
        print 'scanning...'  
        in_filenames = []  
        file_count = 0  
        for file in os.listdir(sys.path[0]):  
            if file.lower().endswith('[all].txt'):  
                os.remove(file)  
            elif file.lower().endswith('.txt'):  
                in_filenames.append(file)  
                file_count = file_count + 1  
        if len(in_filenames) > 0:  
            print '--------------------------------'  
            print '\n'.join(in_filenames)  
            print '--------------------------------'  
            print '%d part(s) in total.' % file_count  
            book_name = raw_input('enter the book name: ')  
            print 'joining...'  
            join(in_filenames, book_name + '[ALL].TXT')  
        else:  
            print 'nothing found.'  
        msvcrt.getch()  