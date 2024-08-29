import os
from os import path
import glob, os
import sys
try:
    from os import scandir
except ImportError:
    from scandir import scandir


err1 = 'No stats inputed'
count = 0
cnt = 0

somestats = [] 
# DEFAULT STATS TO BE USED
defstats  = [ " displayText: ",
              " displayDescription: ",
              " maxHp: ",
              " maxShield: ",
              " price: ",
              " buildSpeed: ",
              " maxAttackRange: ",
              " directDamage: ",
              " areaDamage: ",
              " moveSpeed: "
              " maxTurnSpeed: "
              ]

# DEFAULT PATHS TO BE USED
defpath = './input/MOD'

outpath = './output'


# PROMPT FOR GENERATION
unit_stats = input(">>> PRESS ENTER TO GENERATE UNIT JS FILES \n") # INPUT STRINGS TO BE FOUND SEPERATED BY COMMAS
if (unit_stats): # CHECKS FOR THE STAT INPUT IF ANY

    somestats.append(unit_stats)
    print(somestats[0])
    
else:
    print('>>> Umm uh..')
    
print('> Executing main process...')
# FIND ALL DIRECTORIES IN THE DEFAULT PATH
# CHEERS TO https://stackoverflow.com/users/68707/ben-hoyt FOR THIS GLORIOUS CODE SNIPPET

def scantree(path):
    """Recursively yield DirEntry objects for given directory."""
    for entry in scandir(path):
        if not entry.name.startswith('.') and entry.is_dir(follow_symlinks=False):
            yield from scantree(entry.path)  # see below for Python 2.x
        else:
            yield entry

if __name__ == '__main__':
    for entry in scantree(sys.argv[1] if len(sys.argv) > 1 else '.'):

        # PRINT ALL THE INI FILES AND COUNT THEM
        if entry.is_file() and entry.name.endswith('.ini'):

            count = count + 1      
            print(count, entry.path)
            # WRITE THE JS FILES IN OUTPUT
            with open(entry.path, encoding="utf8") as file:
                name = False
                one = False
                two = False
                three = False
                four = False    
                for line in file:
                    #DECLARE VARIABLES 
                  
                    if not name == True:

                        if 'name: ' in line:
                            if not ',' in line:
                                        fs = open('./output/'+entry.name+'.js',"a+")
                                        ini = line.split('name:')[1].replace("c_","").replace("cexper","exper").replace("-", "")
                                        fs.write("exports.code = function(){ \n")
                                        fs.write("    client.on('messageCreate', message => {\n")
                                        fs.write("            if (message.content.toLowerCase() === " + f"'/{ini}".replace(" ","").lower().rstrip() + "') { \n")
                                        fs.write("              if(message.author.bot) return; \n")
                                        fs.write("              if(message.channel.id === '711753641433759774' || message.channel.id === '606586202942079023') return; \n")
                                        fs.write("              message.channel.send(" + f"{ini}".replace(" ","").rstrip() + "); \n")
                                        fs.write("	          }\n")
                                        fs.write("	 });\n")
                                        fs.write("\nconst " + f"{ini}".replace(" ","").rstrip() + " = new Discord.MessageEmbed()\n")
                                        fs.write("   .setColor('#1500f7') \n")
                                        fs.write("   .setAuthor({name:'Lemons#5444', icon:'https://imgur.com/6NICs3U.png'}) \n")
                                        fs.write("   .setThumbnail('https://camo.githubusercontent.com/7203f752f0f936475f4ac41dcd3ef9d93af9c2452176a05a1e2b081d1a255ef1/68747470733a2f2f63646e2e646973636f72646170702e636f6d2f69636f6e732f3630363538363230323934323037393031372f34323362346662626563663162626164353566653631343638303337623334642e776562703f73697a653d313238')\n")
                                        fs.write("//   .attachFiles(['./code/units/resources/" +  f"{count}" +".png']) \n")
                                        fs.write("//   .setImage('attachment://" +  f"{count}" +".png') \n")
                                        fs = open('./output/LIST.txt',"a+")
                                        fs.writelines(f"{ini}".replace(" ","").replace("null","").lower().rstrip() + ",")
                                        name = True
                    if not one == True:
                        if 'displayText:' in line:
                                            fs = open('./output/'+entry.name+'.js',"a+")
                                            dt = line.split('displayText:')[1]
                                            fs.writelines(f"   .setTitle('{dt}".rstrip() + "') \n")

                        elif 'displayDescription:' in line:
                                            fs = open('./output/'+entry.name+'.js',"a+")
                                            dd = line.split('displayDescription:')[1].replace("'","")
                                            fs.writelines(f"   .setDescription('{dd}".rstrip() + "') \n")
                                            #fs.writelines("   .addField('Stats','\\u2800') \n")
                                            one = True
                    if not two == True:
                        if 'maxHp:' in line:
                                            fs = open('./output/'+entry.name+'.js',"a+")
                                            hp = line.split('maxHp:')[1]
                                            fs.writelines(f"   .addField('Health: {hp}".rstrip() + "','\\u2800')\n")

                        elif 'maxShield:' in line:
                                            fs = open('./output/'+entry.name+'.js',"a+")
                                            ms = line.split('maxShield:')[1]
                                            fs.writelines(f"   .addField('Shield: {ms}".rstrip() + "','\\u2800')\n")
                                            two = True
                                            

                    if not three == True:
                            if 'directDamage:' in line:
                                                fs = open('./output/'+entry.name+'.js',"a+")
                                                dmg = line.split('directDamage:')[1]
                                                fs.writelines(f"   .addField('Direct Damage: {dmg}".rstrip() + "','\\u2800')\n") 

                            elif 'areaDamage:' in line:
                                                fs = open('./output/'+entry.name+'.js',"a+")
                                                admg = line.split('areaDamage:')[1]
                                                fs.writelines(f"   .addField('Area Damage: {admg}".rstrip() + "','\\u2800')\n") 

                            elif 'maxAttackRange:' in line:
                                                fs = open('./output/'+entry.name+'.js',"a+")
                                                rg = line.split('maxAttackRange:')[1]
                                                fs.writelines(f"   .addField('Range: {rg}".rstrip() + "','\\u2800')\n") 
                                                
                            elif 'moveSpeed:' in line:
                                                fs = open('./output/'+entry.name+'.js',"a+")
                                                mvs = line.split('moveSpeed:')[1]
                                                fs.writelines(f"   .addField('Move Speed: {mvs}".rstrip() + "','\\u2800')\n")
                                                three = True 
                    if not four == True:
                            if 'buildSpeed' in line:
                                            fs = open('./output/'+entry.name+'.js',"a+")
                                            bs = line.split('buildSpeed:')[1]
                                            fs.writelines(f"   .addField('Build Speed: {bs}".rstrip() + "','\\u2800')\n")

                            elif 'price:' in line:
                                            fs = open('./output/'+entry.name+'.js',"a+")
                                            pr = line.split('price:')[1]
                                            fs.writelines(f"   .addField('Price: {pr}".rstrip() + "','\\u2800')\n")
                                            four = True
                        
                    elif 'maxTurnSpeed:' in line:
                                            fs = open('./output/'+entry.name+'.js',"a+")
                                            mts = line.split('maxTurnSpeed:')[1]
                                            fs.writelines(f"   .addField('Turn Speed: {mts}".rstrip() + "','\\u2800')\n")   
                fs = open('./output/'+entry.name+'.js',"a+")
                fs.writelines("   .setTimestamp() \n")
                fs.writelines("}\n")
                



                fs = open('./output/$LOADER.js',"a+")
                cnt = cnt + 1
                fs.write("var L2HJ" + f"{count}" + " = require('./" + entry.name + ".js');\n")
                fs.writelines("L2HJ" + f"{count}" + ".code()\n")  
                fs.close()
                
                
