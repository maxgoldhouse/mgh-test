#!/usr/bin/python
# -*- coding: utf-8 -*-
EN_SITEDIR = "./deploy/EN/static/"
EN_TEMPLATEFOLDER = "./templates/en-templates/"
DE_SITEDIR = "./deploy/DE/static/"
DE_TEMPLATEFOLDER = "./templates/de-templates/"
NL_SITEDIR = "./deploy/NL/static/"
NL_TEMPLATEFOLDER = "./templates/nl-templates/"
FR_SITEDIR = "./deploy/FR/static/"
FR_TEMPLATEFOLDER = "./templates/fr-templates/"
ES_SITEDIR = "./deploy/ES/static/"
ES_TEMPLATEFOLDER = "./templates/es-templates/"

MORTGAGE_LTV = 0.75 # Borrow 75% of property value
MORTGAGE_TERM = 15 #years
MORTGAGE_INTEREST = 3.0

PPP = 200 #props per page

trans_proptypes  = {}
trans_proptypes['apartment'] = {'de':'Wohnung','nl':'Appartement','no':'Leilighet','es':'Apartamento','fr':'Appartement'}
trans_proptypes['detached villa'] ={'de':'Freistehende Villa','nl':'Vrijstaande woning','no':'frittliggende Villa','es':'Chalet','fr':'Maison individuelle'}
trans_proptypes['villa'] = {'de':'Villa','nl':'Villa','no':'Villa','es':'Chalet','fr':'Villa'}
trans_proptypes['quadhouse'] = {'de':'Quadhouse','nl':'kwadranthuis','no':'Quadhouse','es':'Quadhouse','fr':'Maison a Quatre'}
trans_proptypes['semi detached villa'] = {'de':'Doppelhaus Villa','nl':'half losstaande villa','no':'Tomannsbolig Villa','es':'Semi-adosada','fr':'Villa jumelée'}
trans_proptypes['semidetached villa'] = {'de':'Doppelhaus Villa','nl':'half losstaande villa','no':'Tomannsbolig Villa','es':'Semi-adosada','fr':'Villa jumelée'}
trans_proptypes['finca'] = {'de':'Landhaus','nl':'landhuis','no':'Herreg&aring;Rd','es':'Finca','fr':'Maisons de campagne'}
trans_proptypes['townhouse'] = {'de':'Reihenhauser','nl':'Geschakelde woning','no':'Rekkehus','es':'Casa de Pueblo','fr':'Maison mitoyenne'}
trans_proptypes['restaurant'] = {'de':'Restaurant','nl':'restaurant','no':'Restaurant','es':'Restaurante','fr':'Restaurant'}
trans_proptypes['commercial'] = {'de':'Gewerbeimmobilien','nl':'Commercieel','no':'Kommersielle eiendommer','es':'Propiedades comerciales','fr':'Batimen commerciaux'}
trans_proptypes['garage'] = {'de':'Garage','nl':'garage','no':'Garasje','es':'Garaje','fr':'Garage'}


trans_search_proptypes = {}
trans_search_proptypes['Apartments'] = {'de':'Ferienwohnungen','nl':'Leilighet','no':'Leiligheter','es':'Apartamentos','fr':'Appartements'}
trans_search_proptypes['Townhouses'] = {'de':'Reihenh&auml;user','nl':'Geschakelde woning','no':'Rekkehus','es':'Casas de Pueblo','fr':'Maisons mitoyennes'}
trans_search_proptypes['Semi Detached Villa'] = {'de':'Villen','nl':'half losstaande villa','no':'','es':'Precio','fr':'Villas jumelée'}
trans_search_proptypes['Detached Villa'] = {'de':'Villen','nl':'Vrijstaande woning','no':'','es':'Precio','fr':'Maison individuelle'}
trans_search_proptypes['Quadhouse'] = {'de':'Quadhouse','nl':'kwadranthuis','no':'','es':'Precio','fr':'Maison a Quatre'}
trans_search_proptypes['Fincas and Rural'] = {'de':'L&auml;ndliche Landh&auml;user','nl':'Fincas en landhuizen','no':'Landlig herreg&aring;rder','es':'Precio','fr':'Maisons de campagne'}
trans_search_proptypes['Beachfront'] = {'de':'Strandh&auml;user','nl':'Zicht op zee','no':'strand hus','es':'Hogares de playa','fr':'Maisons de plage'}
trans_search_proptypes['Golf Property'] = {'de':'Golf H&auml;user','nl':'Huis op de golf','no':'Golf Hjem','es':'Casas de Golf','fr':'Maisons de golf'}
trans_search_proptypes['Commercial properties'] = {'de':'Gewerbeimmobilien','nl':'Commercieel vastgoed','no':'Kommersielle eiendommer','es':'Propiedades comerciales','fr':'Locaux commerciaux'}
trans_search_proptypes['Key Ready and New'] = {'de':'Neubau schl&uuml;sselfertig','nl':'nieuwbouw','no':'Nybygde Boliger','es':'Casas Nuevas','fr':'Maisons nouvellement construites'}
trans_search_proptypes['Penthouse'] = {'de':'Penthouse-Wohnungen','nl':'Penthouse/dakappartement','no':'Penthouse leilighetene','es':'&Aacute;tico','fr':'Penthouse'}
trans_search_proptypes['Luxury Property'] = {'de':'Luxus-Wohnungen','nl':'Luxehuizen','no':'luksusboliger','es':'Casas de lujo','fr':'Propri&eacute;t&eacute; de Prestige'}

trans_features = {}
trans_features['Long term Rentals'] = {'de':'Langfristige Vermietungen','nl':'Leilighet','no':'Langtidsleie','es':'Louer pour long terme'}
trans_features['for sale'] = {'de':'zu verkaufen','nl':'Leilighet','no':'til salgs','es':'en venta', 'fr':'a vendre'}
trans_features['for rent'] = {'de':'zu lassen','nl':'Leilighet','no':'til leie','es':'alquiler','fr':'a louer'}
trans_features['price'] = {'de':'Preis','nl':'Leilighet','no':'','es':'Precio','fr':'Prix'}
trans_features['bathroom']={'de':'Bad','nl':'Leilighet','no':'','es':'Ba&ntilde;o','fr':'bain'}
trans_features['bed'] = {'de':'Schlafz','nl':'Leilighet','no':'','es':'Dormitorio','fr':'chambre'}
trans_features['swimming pool'] = {'de':'Schwimmbad','nl':'Leilighet','no':'','es':'Picina','fr':'piscene'}
