print("Enter temperature")
while(True):

    temp = input()

    with open('room_temp.config', 'w+') as f:
            f.writelines([
                '## COMMENT TEMPERATURE WHEN USING RANDOM AND VICE VERSA ## \n',
                '\n\n',
                '# TEMPERATURE 26 <- EXAMPLE \n'
            ])
            f.write('TEMPERATURE {} \n'.format(temp))
            f.writelines([
                '\n',
                '# RANDOM TEMPERATURE 12 42   <- EXAMPLE\n',
                '# RANDOM TEMPERATURE 12 42'
                ])
        
            f.close()