#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys);
sys.setdefaultencoding("utf8")
sys.path.insert(0, './')
import jinja2
import os
import _all_rubrunsdata
import _mghsettings
import _mgh_data

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

templateLoader = jinja2.FileSystemLoader(_mghsettings.DE_TEMPLATEFOLDER)
templateEnv = jinja2.Environment( loader=templateLoader )

TEMPLATE_FILE = "de_proplist.jinja"

template = templateEnv.get_template( TEMPLATE_FILE )

def makepage(propdict,prevpage,nextpage,thispage, pagename_en, pagename_de, pagename_nl, pagename_fr):
	propdict['prevpage'] = pagename_de+str(prevpage)+".html"
	propdict['nextpage'] = pagename_de+str(nextpage)+".html"
	propdict['url_en'] = pagename_en+str(thispage)+".html"
	propdict['url_de'] = pagename_de+str(thispage)+".html"
	propdict['url_nl'] = pagename_nl+str(thispage)+".html"
	propdict['url_fr'] = pagename_fr+str(thispage)+".html"
	outputText = template.render(propdict)
	#print outputText
	file = open(_mghsettings.DE_SITEDIR+pagename_de+str(thispage)+".html", "w")
	file.write(outputText)
	file.close()

for rubrun in _all_rubrunsdata.rubruns:
	topsixdict = {}
	topsixdict['title'] = rubrun["DE"]['title']
	topsixdict['keywords'] = rubrun["DE"]['keywords']
	topsixdict['description'] = rubrun["DE"]['description']
	topsixdict['h1'] = rubrun["DE"]['h1']
	topsixdict['props'] = []

	rowcount = 0
	pagecount = 0
	for propinlist in _mgh_data.proplists[rubrun['rubrun']]:# LIMIT 20
		rowcount = rowcount + 1
		row = _mgh_data.props[str(propinlist)]
		de_proptype = _mghsettings.trans_proptypes[row['ptype'].lower()]['de']
		#propurl_nl = '/'+str(row['intbeds'])+'-slaapkamer-'+nl_proptype.replace(' ','-').replace('&auml;','a')+'-in-'+row['strlocation_detail'].replace(' ','-')+'-'+row['strpropertyid']+'.html'
		propurl = '/'+str(row['beds'])+'-bad-'+de_proptype.replace(' ','-').replace('&auml;','a')+'-in-'+row['location'].replace(' ','-')+'-'+row['pid']+'.html'

		if row['rental'] == 'True':
			saleorrent = 'zu vermieten'
		else:
			saleorrent = 'zu verkaufen'
		prop = {}
		if row['DE'][:400][-1] == '\xc3':
		  prop['description'] = row['DE'][:399]
		else:
		  prop['description'] = row['DE'][:400]
		prop['beds'] = row['beds']
		prop['baths'] = row['baths']
		prop['propid'] = row['pid']
		prop['propref'] = row['ref']
		prop['propurl'] = propurl
		prop['locationdetail']=row['location']
		prop['proptype']= de_proptype
		prop['saleorrent']=saleorrent
		if row['frequency'] == 'week':
			prop['frequency'] = ' je Woche'
		elif row['frequency'] == 'month':
			prop['frequency'] = ' je Monat'
		else:
			prop['frequency']= ''
		prop['underoffersold'] = row['salestage']
		if row['salestage'] == '0':
			prop['price'] = "<span class='price_eur'>&euro;"+"{:,}".format(int(row['price']))+"</span> "
		elif row['salestage'] == '2':
			prop['price'] = 'verkauft'
		elif row['salestage'] == '3':
			prop['price'] = '<span style="color:red;">VERMIETET</span>'
			prop['frequency'] = ''
		else:
			prop['price'] = ''
		prop['img'] = row['pics'][0].replace('/s0/','/s400/')
		topsixdict['props'].append(prop)

		if rowcount == _mghsettings.PPP:
			rowcount = 0
			propstoprocess = propstoprocess - _mghsettings.PPP
			print propstoprocess
			pagenext = pagecount+1
			pageprev = pagecount-1
			if propstoprocess < _mghsettings.PPP:
				pagenext = 0
			if pageprev < 0:
				pageprev = 0
			makepage(topsixdict,pageprev,pagenext,pagecount,rubrun['pagename_en'],rubrun['pagename_de'],rubrun['pagename_nl'],rubrun['pagename_fr'])
			pagecount = pagecount + 1
			topsixdict['props'] = []



	if len(topsixdict) > 0:
		makepage(topsixdict,pagecount-1,0,pagecount,rubrun['pagename_en'],rubrun['pagename_de'],rubrun['pagename_nl'],rubrun['pagename_fr'])



#for item in topsixdict['props']:
	#for key in item:
		#print item[key]

	#"""

	#title 'Villamartin Property for Sale, Playa Flamenca, Cabo Roig, Guardamar del Segura, Ciudad Quesada Costa Blanca Spain'
	#keywords 'Villamartin Property for sale, Playa Flamenca, Cabo Roig, Guardamar del Segura and Ciudad Quesada'
	#description  'Property for sale in Villamartin, Playa Flamenca, Cabo Roig, Los Altos, Los Balcones, Guardamar del Segura, Ciudad Quesada in Torrevieja and  Orihuela Costa areas of Southern Costa Blanca Spain, '

	#propurl '/'+row['strpropertyid']+'-'+row['intbeds']+' bed '+row['strpropertytype']+' in '+row['strlocation_detail']+'.html'
	#locationdetail row['strlocation_detail']
	#proptype row['strpropertytype']
	#saleorrent if row['blnrental'] == 1 saleorrent = 'For rent' else saleorrent = 'For Sale'
	#price row['intprice']

	#"""
