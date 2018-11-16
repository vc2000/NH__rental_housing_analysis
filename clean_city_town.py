import pandas as pd
tc_list=[]
with open('nh_town_city.txt') as file:
    for line in file:
        tc_list.append(line.replace('\n','').lower())
df= pd.read_csv("halfclean(5).csv", encoding="ISO-8859-1")



df=df.replace({'City':r'^.*acworth.*$'}, {'City':'acworth'}, regex=True)
df=df.replace({'City':r'^.*allenstown.*$'}, {'City':'allenstown'}, regex=True)
df=df.replace({'City':r'^.*andover.*$'}, {'City':'andover'}, regex=True)
df=df.replace({'City':r'^.*atkinson.*$'}, {'City':'atkinson'}, regex=True)


df=df.replace({'City':r'^.*bedford.*$'}, {'City':'bedford'}, regex=True)
df=df.replace({'City':r'^.*belmont.*$'}, {'City':'belmont'}, regex=True)
df=df.replace({'City':r'^.*bethlehem.*$'}, {'City':'bethlehem'}, regex=True)
df=df.replace({'City':r'^.*berlin.*$'}, {'City':'berlin'}, regex=True)
df=df.replace({'City':r'^.*bow.*$'}, {'City':'bow'}, regex=True)
df=df.replace({'City':r'^.*bradford.*$'}, {'City':'bradford'}, regex=True)
df=df.replace({'City':r'^.*brentwood.*$'}, {'City':'brentwood'}, regex=True)
df=df.replace({'City':r'^.*brookline.*$'}, {'City':'brookline'}, regex=True)


df=df.replace({'City':r'^.*campton.*$'}, {'City':'campton'}, regex=True)
df=df.replace({'City':r'^.*carroll.*$'}, {'City':'carroll'}, regex=True)
df=df.replace({'City':r'^.*chesterfield.*$'}, {'City':'chesterfield'}, regex=True)
df=df.replace({'City':r'^.*claremont.*$'}, {'City':'claremont'}, regex=True)
df=df.replace({'City':r'^.*colebrook.*$'}, {'City':'colebrook'}, regex=True)
df=df.replace({'City':r'^.*concord.*$'}, {'City':'concord'}, regex=True)
df=df.replace({'City':r'^.*conway.*$'}, {'City':'conway'}, regex=True)

df=df.replace({'City':r'^.*danville.*$'}, {'City':'danville'}, regex=True)
df=df.replace({'City':r'^.*deering.*$'}, {'City':'deering'}, regex=True)
df=df.replace({'City':r'^.*derry.*$'}, {'City':'derry'}, regex=True)
df=df.replace({'City':r'^.*dover.*$'}, {'City':'dover'}, regex=True)
df=df.replace({'City':r'^.*dublin.*$'}, {'City':'dublin'}, regex=True)
df=df.replace({'City':r'^.*dunbarton.*$'}, {'City':'dunbarton'}, regex=True)
df=df.replace({'City':r'^.*durham.*$'}, {'City':'durham'}, regex=True)

df=df.replace({'City':r'^.*enfield.*$'}, {'City':'enfield'}, regex=True)
df=df.replace({'City':r'^.*epping.*$'}, {'City':'epping'}, regex=True)
df=df.replace({'City':r'^.*epsom.*$'}, {'City':'epsom'}, regex=True)
df=df.replace({'City':r'^.*exeter.*$'}, {'City':'exeter'}, regex=True)

df=df.replace({'City':r'^.*farmington.*$'}, {'City':'farmington'}, regex=True)
df=df.replace({'City':r'^.*franconia.*$'}, {'City':'franconia'}, regex=True)
df=df.replace({'City':r'^.*franklin.*$'}, {'City':'franklin'}, regex=True)
df=df.replace({'City':r'^.*fremont.*$'}, {'City':'fremont'}, regex=True)

df=df.replace({'City':r'^.*goffstown.*$'}, {'City':'goffstown'}, regex=True)
df=df.replace({'City':r'^.*goshen.*$'}, {'City':'goshen'}, regex=True)
df=df.replace({'City':r'^.*greenfield.*$'}, {'City':'greenfield'}, regex=True)

df=df.replace({'City':r'^.*hampstead.*$'}, {'City':'hampstead'}, regex=True)
df=df.replace({'City':r'^.*hampton.*$'}, {'City':'hampton'}, regex=True)
df=df.replace({'City':r'^.*hancock.*$'}, {'City':'hancock'}, regex=True)
df=df.replace({'City':r'^.*hanover.*$'}, {'City':'hanover'}, regex=True)
df=df.replace({'City':r'^.*haverhill.*$'}, {'City':'haverhill'}, regex=True)
df=df.replace({'City':r'^.*henniker.*$'}, {'City':'henniker'}, regex=True)
df=df.replace({'City':r'^.*holderness.*$'}, {'City':'holderness'}, regex=True)
df=df.replace({'City':r'^.*hillsboro.*$'}, {'City':'hillsboro'}, regex=True)
df=df.replace({'City':r'^.*hollis.*$'}, {'City':'hollis'}, regex=True)
df=df.replace({'City':r'^.*hooksett.*$'}, {'City':'hooksett'}, regex=True)
df=df.replace({'City':r'^.*hopkinton.*$'}, {'City':'hopkinton'}, regex=True)
df=df.replace({'City':r'^.*hudson.*$'}, {'City':'hudson'}, regex=True)

df=df.replace({'City':r'^.*jackson.*$'}, {'City':'jackson'}, regex=True)

df=df.replace({'City':r'^.*kensington.*$'}, {'City':'kensington'}, regex=True)
df=df.replace({'City':r'^.*keene.*$'}, {'City':'keene'}, regex=True)
df=df.replace({'City':r'^.*kingston.*$'}, {'City':'kingston'}, regex=True)

df=df.replace({'City':r'^.*laconia.*$'}, {'City':'laconia'}, regex=True)
df=df.replace({'City':r'^.*lebanon.*$'}, {'City':'lebanon'}, regex=True)
df=df.replace({'City':r'^.*lincoln.*$'}, {'City':'lincoln'}, regex=True)
df=df.replace({'City':r'^.*lisbon.*$'}, {'City':'lisbon'}, regex=True)
df=df.replace({'City':r'^.*littleton.*$'}, {'City':'littleton'}, regex=True)
df=df.replace({'City':r'^.*londonderry.*$'}, {'City':'londonderry'}, regex=True)

df=df.replace({'City':r'^.*manchester.*$'}, {'City':'manchester'}, regex=True)
df=df.replace({'City':r'^.*madison.*$'}, {'City':'madison'}, regex=True)
df=df.replace({'City':r'^.*marlow.*$'}, {'City':'marlow'}, regex=True)
df=df.replace({'City':r'^.*merrimack.*$'}, {'City':'merrimack'}, regex=True)
df=df.replace({'City':r'^.*milford.*$'}, {'City':'milford'}, regex=True)
df=df.replace({'City':r'^.*milton.*$'}, {'City':'milton'}, regex=True)


df=df.replace({'City':r'^.*nashua.*$'}, {'City':'nashua'}, regex=True)
df=df.replace({'City':r'^.*new boston.*$'}, {'City':'new boston'}, regex=True)
df=df.replace({'City':r'^.*newbury.*$'}, {'City':'newbury'}, regex=True)
df=df.replace({'City':r'^.*new castle.*$'}, {'City':'new castle'}, regex=True)
df=df.replace({'City':r'^.*new london.*$'}, {'City':'new london'}, regex=True)
df=df.replace({'City':r'^.*newmarket.*$'}, {'City':'newmarket'}, regex=True)
df=df.replace({'City':r'^.*newport.*$'}, {'City':'newport'}, regex=True)
df=df.replace({'City':r'^.*newton.*$'}, {'City':'newton'}, regex=True)
df=df.replace({'City':r'^.*northwood.*$'}, {'City':'northwood'}, regex=True)

df=df.replace({'City':r'^.*ossipee.*$'}, {'City':'ossipee'}, regex=True)

df=df.replace({'City':r'^.*pelham.*$'}, {'City':'pelham'}, regex=True)
df=df.replace({'City':r'^.*pembroke.*$'}, {'City':'pembroke'}, regex=True)
df=df.replace({'City':r'^.*peterborough.*$'}, {'City':'peterborough'}, regex=True)
df=df.replace({'City':r'^.*pittsfield.*$'}, {'City':'pittsfield'}, regex=True)
df=df.replace({'City':r'^.*plaistow.*$'}, {'City':'plaistow'}, regex=True)
df=df.replace({'City':r'^.*plymouth.*$'}, {'City':'plymouth'}, regex=True)
df=df.replace({'City':r'^.*portsmouth.*$'}, {'City':'portsmouth'}, regex=True)

df=df.replace({'City':r'^.*raymond.*$'}, {'City':'raymond'}, regex=True)
df=df.replace({'City':r'^.*rindge.*$'}, {'City':'rindge'}, regex=True)
df=df.replace({'City':r'^.*rochester.*$'}, {'City':'rochester'}, regex=True)
df=df.replace({'City':r'^.*rollinsford.*$'}, {'City':'rollinsford'}, regex=True)
df=df.replace({'City':r'^.*rye.*$'}, {'City':'rye'}, regex=True)

df=df.replace({'City':r'^.*salem.*$'}, {'City':'salem'}, regex=True)
df=df.replace({'City':r'^.*sandown.*$'}, {'City':'sandown'}, regex=True)
df=df.replace({'City':r'^.*seabrook.*$'}, {'City':'seabrook'}, regex=True)
df=df.replace({'City':r'^.*somersworth.*$'}, {'City':'somersworth'}, regex=True)
df=df.replace({'City':r'^.*sunapee.*$'}, {'City':'sunapee'}, regex=True)

df=df.replace({'City':r'^.*temple.*$'}, {'City':'temple'}, regex=True)
df=df.replace({'City':r'^.*tilton.*$'}, {'City':'tilton'}, regex=True)
df=df.replace({'City':r'^.*troy.*$'}, {'City':'troy'}, regex=True)
df=df.replace({'City':r'^.*twin mountain.*$'}, {'City':'twin mountain'}, regex=True)

df=df.replace({'City':r'^.*walpole.*$'}, {'City':'walpole'}, regex=True)
df=df.replace({'City':r'^.*warner.*$'}, {'City':'warner'}, regex=True)
df=df.replace({'City':r'^.*washington.*$'}, {'City':'washington'}, regex=True)
df=df.replace({'City':r'^.*waterville valley.*$'}, {'City':'waterville valley'}, regex=True)
df=df.replace({'City':r'^.*weare.*$'}, {'City':'weare'}, regex=True)
df=df.replace({'City':r'^.*weirs beach.*$'}, {'City':'weirs beach'}, regex=True)
df=df.replace({'City':r'^.*whitefield.*$'}, {'City':'whitefield'}, regex=True)
df=df.replace({'City':r'^.*windham.*$'}, {'City':'windham'}, regex=True)
df=df.replace({'City':r'^.*wolfeboro.*$'}, {'City':'wolfeboro'}, regex=True)
df=df.replace({'City':r'^.*woodstock.*$'}, {'City':'woodstock'}, regex=True)

df.to_csv("halfclean(6).csv", encoding='utf-8', index=False)
