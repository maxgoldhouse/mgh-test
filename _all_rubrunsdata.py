#!/usr/bin/python
# -*- coding: utf-8 -*-
rubruns=[
{
"rubrun":"All",
"query":"Select * FROM mghprops WHERE blndisplay = 1 AND blnrental = 0 ORDER BY intprice ASC",
"EN":{
"description":"Villas, Apartments, Townhouses and Fincas for sale in Villamartin, Playa Flamenca, Cabo Roig, Los Altos, Los Balcones, Guardamar del Segura, Ciudad Quesada in Torrevieja and  Orihuela Costa areas of Southern Costa Blanca Spain",
"keywords":"Villamartin Villas, Apartments, Townhouses and Fincas, Playa Flamenca, Cabo Roig, Guardamar del Segura and Ciudad Quesada",
"title":"Villas, Apartments, Townhouses and Fincas for Sale, Playa Flamenca, Cabo Roig, Guardamar del Segura, Ciudad Quesada Costa Blanca Spain",
"h1":"Property For Sale in Villamartin, Cabo Roig, Torrevieja, Playa Flamenca and Orihuela Costa Spain"},
"FR":{
"description":"Villas, appartements, maisons mitoyennes et fincas à vendre à Villamartin, Playa Flamenca, Cabo Roig, Los Altos, Los Balcones, Guardamar del Segura, Ciudad Quesada, Torrevieja et Costa Blanca Sud, Espagne",
"keywords":"Villas, appartements, maisons mitoyennes et fincas à Villamartin, Playa Flamenca, Cabo Roig, Guardamar del Segura et Ciudad Quesada",
"title":"Villas, appartements, maisons mitoyennes et fincas à vendre à Playa Flamenca, Cabo Roig, Guardamar del Segura et Ciudad Quesada, Costa Blanca Sud",
"h1":"Propriétét à vendre à Villamartin, Cabo Roig, Torrevieja, Playa Flamenca et Orihuela Costa, Espagne"
},
"DE":{
"description":"Villas, Ferienwohnungen, Stadth&auml;user und Fincas zu verkaufen in Villamartin, Playa Flamenca, Cabo Roig, Los Altos, Los Balcones, Guardamar del Segura, Ciudad Quesada in Torrevieja and  Orihuela Costa areas of Southern Costa Blanca Spanien",
"keywords":"Villamartin Villas, Ferienwohnungen, Stadth&auml;user und Fincas, Playa Flamenca, Cabo Roig, Guardamar del Segura und Ciudad Quesada",
"title":"Villas, Ferienwohnungen, Stadth&auml;user und Fincas zu verkaufen, Playa Flamenca, Cabo Roig, Guardamar del Segura, Ciudad Quesada Costa Blanca Spanien",
"h1":"Immobilien zu verkaufen in Villamartin, Cabo Roig, Torrevieja, Playa Flamenca und Orihuela Costa Spanien"
},
"NL":{
"description":"Villa's, appartementen, geschakelde woningen en finca's te koop in Villamartin, Playa Flamenca, Cabo Roig, Los Altos, Los Balcones, Guardamar del Segura, Ciudad Quesada, Torrevieja en Costa Blanca Zuid, Spanje",
"keywords":"Villa's, appartementen geschakelde woningen en finca's in Villamartin, Playa Flamenca, Cabo Roig, Guardamar del Segura en Ciudad Quesada",
"title":"Villa's, appartementen, geschakelde woningen en finca's te koop in Playa Flamenca, Cabo Roig, Guardamar del Segura, Ciudad Quesada, Costa Blanca Zuid",
"h1":"Eigendom te koop in Villamartin, Cabo Roig, Torrevieja, Playa Flamenca en Orihuela Costa, Spanje"
},
"pagename_en":"villas-apartments-townhouses-and-fincas-for-sale-",
"pagename_nl":"villas-appartementen-geschakelde-woningen-en-fincas-te-koop-",
"pagename_fr":"Villas-appartements-maisons-mitoyennes-et-fincas-a-vendre-",
"pagename_de":"villas-Ferienwohnungen-Stadthauser-und-fincas-zu-verkaufen-"
},
{
"rubrun":"0-1",
"query":"Select * FROM mghprops WHERE blndisplay = 1 AND blnrental = 0 AND intprice <= 100000 ORDER BY intprice ASC",
"EN":{
"description":"Villas, apartments, townhouses and spanish homes for less than &euro;100,000",
"keywords":"Bargain Villas, Bargain apartments, Cheap Costa Blanca apartments and townhouses",
"title":"Costa Blanca Property for less than &euro;100,000",
"h1":"Property For Sale in Villamartin, Cabo Roig, Torrevieja, Playa Flamenca Costa Blanca South priced below &euro;100,000"},
"FR":{
"description":"Villas, appartements, maisons mitoyennes et fincas jusqu à 100 000 euros",
"keywords":"Villas à bas prix, appartements à bas prix, maisons mitoyennes à bas prix Costa Blanca",
"title":"Propriété à Costa Blanca jusqu'à 100 000 euros",
"h1":"Propriété à vendre à Villamartin, Cabo Roig, Torrevieja, Playa Flamenca, Costa Blanca Sud jusqu'à 100 000 euros"
},
"DE":{
"description":"Villas, Ferienwohnungen, Stadth&auml;user und spanisch H&auml;user f&uuml;r weniger als &euro;100,000",
"keywords":"Schn&auml;ppchen Villas, Schn&auml;ppchen Ferienwohnungen, Schn&auml;ppchen Costa Blanca Ferienwohnungen und Stadth&auml;user",
"title":"Costa Blanca Immobilien f&uuml;r weniger als &euro;100,000",
"h1":"Immobilien zu verkaufen in Villamartin, Cabo Roig, Torrevieja, Playa Flamenca Costa Blanca S&uuml;d f&uuml;r weniger als &euro;100,000"
},
"NL":{
"description":"Villa's, appartementen, geschakelde woningen en Spaanse huizen tot 100.000 euro",
"keywords":"Goedkope villa's, goedkope appartementen, goedkope appartementen en geschakelde woningen Costa Blanca",
"title":"Eigendom aan de Costa Blanca tot 100.000 euro",
"h1":"Eigendom te koop in Villamartin, Cabo Roig, Torrevieja, Playa Flamenca, Costa Blanca Zuid tot &euro;100.000"
},
"pagename_en":"costa-blanca-property-for-less-than-100000-",
"pagename_nl":"Eigendom-in-de-Costa-Blanca-tot-100000-euro-",
"pagename_fr":"Propriete-a-Costa-Blanca-jusqu-a-100000-euro-",
"pagename_de":"costa-blanca-Immobilien-fur-weniger-als-100000-"
},
{
"rubrun":"1-2",
"query":"Select * FROM mghprops WHERE blndisplay = 1 AND blnrental = 0 AND intprice >= 101000  AND intprice <= 200000 ORDER BY intprice ASC",
"EN":{
"description":"Villas, apartments, townhouses and spanish homes priced between &euro;100,000 and &euro;200,000",
"keywords":"Affordable Villas, Affordable apartments, Bargaiin Costa Blanca apartments and townhouses",
"title":"Costa Blanca Property priced between &euro;100,000 and &euro;200,000",
"h1":"Property For Sale in Villamartin, Cabo Roig, Torrevieja, Playa Flamenca Costa Blanca South priced between &euro;100,000 and &euro;200,000"},
"FR":{
"description":"Villas, appartements, maisons mitoyennes et fincas de 100 000 euros à 200 000 euros",
"keywords":"Villas à moyen prix, appartements à moyen prix, appartements à bas prix, et maisons mitoyennes Costa Blanca",
"title":"Propriété à Costa Blanca de 100 000 euros à 200 000 euros",
"h1":"Propriété à vendre à Villamartin, Cabo Roig, Torrevieja, Playa Flamenca, Costa Blanca Sud de 100 000 euros à 200 000 euros"
},
"DE":{
"description":"Villas, Ferienwohnungen, Stadth&auml;user und spanisch H&auml;user zwischen &euro;100,000 und &euro;200,000 preislich",
"keywords":"preiswert Villas, preiswert Ferienwohnungen, Schn&auml;ppchen Preisen Costa Blanca Ferienwohnungen und Stadth&auml;user",
"title":"Costa Blanca Immobilien priced zwischen &euro;100,000 und &euro;200,000",
"h1":"Immobilien zu verkaufen in Villamartin, Cabo Roig, Torrevieja, Playa Flamenca Costa Blanca S&uuml;d zwischen &euro;100,000 und &euro; 200,000 preislich"
},
"NL":{
"description":"Villa's, appartementen, geschakelde woningen en Spaanse huizen van 100.000 euro tot 200.000 euro",
"keywords":"Voordelige villa's, voordelige appartementen, goedkope appartementen en geschakelde woningen Costa Blanca",
"title":"Eigendom aan de Costa Blanca van 100.000 euro tot 200.000 euro",
"h1":"Eigendom te koop in Villamartin, Cabo Roig, Torrevieja, Playa Flamenca, Costa Blanca Zuid van &euro;100.000 tot &euro;200.000"
},
"pagename_en":"costa-blanca-property-from-100000-to-200000-",
"pagename_nl":"Eigendom-aan-de-Costa-Blanca-van-100000-tot-200000-euro-",
"pagename_fr":"Propriete-a-Costa-Blanca-de-100000-euro-a-200000-euro-",
"pagename_de":"costa-blanca-Immobilien-von-100000-bis-200000-"
},
{
"rubrun":"2-3",
"query":"Select * FROM mghprops WHERE blndisplay = 1 AND blnrental = 0 AND intprice >= 201000  AND intprice <= 300000 ORDER BY intprice ASC",
"EN":{
"description":"Villas, apartments, townhouses and spanish homes priced between &euro;200,000 and &euro;300,000",
"keywords":"Desirable Villas, Attractive apartments, Wonderful Costa Blanca homes",
"title":"Costa Blanca Property priced between &euro;200,000 and &euro;300,000",
"h1":"Property For Sale in Villamartin, Cabo Roig, Torrevieja, Playa Flamenca Costa Blanca South priced between &euro;200,000 and &euro;300,000"},
"FR":{
"description":"Villas, appartements, maisons mitoyennes et fincas de 200 000 euros à 300 000 euros",
"keywords":"Villas populaires, appartements agréables, et maisons magnifiques Costa Blanca",
"title":"Propriété à Costa Blanca de 200 000 euros à 300 000 euros",
"h1":"Propriété à vendre à Villamartin, Cabo Roig, Torrevieja, Playa Flamenca, Costa Blanca Sud de 200 000 euros à 300 000 euros"
},
"DE":{
"description":"Villas, Ferienwohnungen, Stadth&auml;user and spanisch H&auml;user zwischen &euro;200,000 und &euro; 300,000 preislich",
"keywords":"w&uuml;nschenswert Villas, Attractive Ferienwohnungen, Wunderbare Costa Blanca H&auml;user",
"title":"Costa Blanca Immobilien zwischen &euro;200,000 und &euro; 300,000 preislich",
"h1":"Immobilien zu verkaufen in Villamartin, Cabo Roig, Torrevieja, Playa Flamenca Costa Blanca S&uuml;d zwischen &euro;200,000 und &euro; 300,000 preislich"
},
"NL":{
"description":"Villa's, appartementen, geschakelde woningen en Spaanse huizen van 200.000 euro tot 300.000 euro",
"keywords":"Populaire villa's, aangename appartementen, prachtige huizen Costa Blanca",
"title":"Eigendom aan de Costa Blanca van 200.000 euro tot 300.000 euro",
"h1":"Eigendom te koop in Villamartin, Cabo Roig, Torrevieja, Playa Flamenca, Costa Blanca Zuid van &euro;200.000 tot &euro;300.000"
},
"pagename_en":"costa-blanca-property-from-200000-to-300000-",
"pagename_nl":"Eigendom-aan-de-Costa-Blanca-van-200000-tot-300000-euro-",
"pagename_fr":"Propriete-a-Costa-Blanca-de-200000-euro-a-300000-euro-",
"pagename_de":"costa-blanca-Immobilien-von-200000-bis-300000-"
},
{
"rubrun":"3-4",
"query":"Select * FROM mghprops WHERE blndisplay = 1 AND blnrental = 0 AND intprice >= 301000  AND intprice <= 400000 ORDER BY intprice ASC",
"EN":{
"description":"Villas, apartments, townhouses and spanish homes priced between &euro;300,000 and &euro;400,000",
"keywords":"Very nice Villas, Luxury apartments, Costa Blanca homes for retirement",
"title":"Costa Blanca Property priced between &euro;300,000 and &euro;400,000",
"h1":"Property For Sale in Villamartin, Cabo Roig, Torrevieja, Playa Flamenca Costa Blanca South priced between &euro;300,000 and &euro;400,000"},
"FR":{
"description":"Villas, appartements, maisons mitoyennes et fincas de 300 000 euros à 400 000 euros",
"keywords":"Villas magnifiques, appartements de luxe, et maisons pour retraités Costa Blanca",
"title":"Propriété à Costa Blanca de 300 000 euros à 400 000 euros",
"h1":"Propriété à vendre à Villamartin, Cabo Roig, Torrevieja, Playa Flamenca, Costa Blanca Sud de 300 000 euros à 400 000 euros"
},
"DE":{
"description":"Villas, Ferienwohnungen, Stadth&auml;user and spanisch H&auml;user zwischen &euro;300,000 und &euro; 400,000 preislich",
"keywords":"Very nice Villas, Luxury Ferienwohnungen, Costa Blanca H&auml;user for retirement",
"title":"Costa Blanca Immobilien priced zwischen &euro;300,000 und &euro; 400,000",
"h1":"Immobilien zu verkaufen in Villamartin, Cabo Roig, Torrevieja, Playa Flamenca Costa Blanca S&uuml;d zwischen &euro;300,000 und &euro; 400,000 preislich"
},
"NL":{
"description":"Villa's, appartementen, geschakelde woningen en Spaanse huizen van 300.000 euro tot 400.000 euro",
"keywords":"Prachtige villa's, luxe-appartementen en huizen voor gepensioneerden Costa Blanca",
"title":"Eigendom aan de Costa Blanca van 300.000 euro tot 400.000 euro",
"h1":"Eigendom te koop in Villamartin, Cabo Roig, Torrevieja, Playa Flamenca, en Costa Blanca Zuid van &euro;300.000 tot &euro;400.000"
},
"pagename_en":"costa-blanca-property-from-300000-to-400000-",
"pagename_nl":"Eigendom-aan-de-Costa-Blanca-van-300000-tot-400000-euro-",
"pagename_fr":"Propriete-a-Costa-Blanca-de-300000-euro-a-400000-euro-",
"pagename_de":"costa-blanca-Immobilien-von-300000-bis-400000-"
},
{
"rubrun":"4-5",
"query":"Select * FROM mghprops WHERE blndisplay = 1 AND blnrental = 0 AND intprice >= 401000  AND intprice <= 500000 ORDER BY intprice ASC",
"EN":{
"description":"Apartments, townhouses and Spanish villas priced between &euro;400,000 and &euro;500,000",
"keywords":"Well appointed apartments villas, Costa Blanca homes for comfortable living",
"title":"Costa Blanca Property priced between &euro;400,000 and &euro;500,000",
"h1":"Property For Sale in Villamartin, Cabo Roig, Torrevieja, Playa Flamenca Costa Blanca South priced between &euro;400,000 and &euro;500,000"},
"FR":{
"description":"Villas, appartements, maisons mitoyennes et fincas de 400 000 euros à 500 000 euros",
"keywords":"Appartements et villas bien équipées, maisons confortables Costa Blanca",
"title":"Propriété à Costa Blanca de 400 000 euros à 500 000 euros",
"h1":"Propriété à vendre à Villamartin, Cabo Roig, Torrevieja, Playa Flamenca, Costa Blanca Sud de 400 000 euros à 500 000 euros"
},
"DE":{
"description":"Ferienwohnungen, Stadth&auml;user und spanische villas zwischen &euro;400,000 und &euro; 500,000 preislich",
"keywords":"Well appointed Ferienwohnungen villas, Costa Blanca H&auml;user for comfortable living",
"title":"Costa Blanca Immobilien priced zwischen &euro;400,000 und &euro; 500,000",
"h1":"Immobilien zu verkaufen in Villamartin, Cabo Roig, Torrevieja, Playa Flamenca Costa Blanca S&uuml;d zwischen &euro;400,000 und &euro; 500,000 preislich"
},
"NL":{
"description":"Appartementen, geschakelde woningen en Spaanse villa's van 400.000 euro tot 500.000 euro",
"keywords":"Goed uitgeruste appartementen en villa's, comfortabele huizen Costa Blanca",
"title":"Eigendom aan de Costa Blanca van 400.000 euro tot 500.000 euro",
"h1":"Eigendom te koop in Villamartin, Cabo Roig, Torrevieja, Playa Flamenca, Costa Blanca Zuid van &euro;400.000 tot &euro;500.000"
},
"pagename_en":"costa-blanca-property-from-400000-to-500000-",
"pagename_nl":"Eigendom-aan-de-Costa-Blanca-van-400000-tot-500000-euro-",
"pagename_fr":"Propriete-a-Costa-Blanca-de-400000-euro-a-500000-euro-",
"pagename_de":"costa-blanca-Immobilien-von-400000-bis-500000-"
},
{
"rubrun":"5-6",
"query":"Select * FROM mghprops WHERE blndisplay = 1 AND blnrental = 0 AND intprice >= 501000  AND intprice <= 600000 ORDER BY intprice ASC",
"EN":{
"description":"Apartments, townhouses and Spanish villas priced between &euro;500,000 and &euro;600,000",
"keywords":"Costa Blanca homes, Villas, Apartments, Golf homes, Property South Costa Blanca, Spain",
"title":"Costa Blanca Property priced between &euro;500,000 and &euro;600,000",
"h1":"Property For Sale in Villamartin, Cabo Roig, Campoamor, Playa Flamenca Costa Blanca South priced between &euro;500,000 and &euro;600,000"},
"FR":{
"description":"Villas, appartements, maisons mitoyennes et fincas de 500 000 euros à 600 000 euros",
"keywords":"Maisons Costa Blanca,  villas, appartements, maisons sur le golf resort, propriété Costa Blanca Sud, Espagne",
"title":"Propriété à Costa Blanca de 500 000 euros à 600 000 euros",
"h1":"Propriété à vendre à Villamartin, Cabo Roig, Campoamor, Playa Flamenca, Costa Blanca Sud de 500 000 euros à 600 000 euros"
},
"DE":{
"description":"Ferienwohnungen, Stadth&auml;user und spanische villas zwischen &euro;500,000 und &euro; 600,000 preislich",
"keywords":"Costa Blanca H&auml;user, Villas, Ferienwohnungen, Golf H&auml;user, Immobilien Costa Blanca S&uuml;d, Spanien",
"title":"Costa Blanca Immobilien priced zwischen &euro;500,000 und &euro; 600,000",
"h1":"Immobilien zu verkaufen in Villamartin, Cabo Roig, Campoamor, Playa Flamenca Costa Blanca S&uuml;d zwischen &euro;500,000 und &euro; 600,000 preislich"
},
"NL":{
"description":"Appartementen, geschakelde woningen en Spaanse villa's van 500.000 euro tot 600.000 euro",
"keywords":"Huizen Costa Blanca, villa's, appartementen, huizen aan de golf, eigendommen Costa Blanca Zuid, Spanje",
"title":"Eigendom aan de Costa Blanca van 500.000 euro tot 600.000 euro",
"h1":"Eigendom te koop in Villamartin, Cabo Roig, Campoamor, Playa Flamenca, Costa Blanca Zuid van &euro;500.000 tot &euro;600.000"
},
"pagename_en":"costa-blanca-property-from-500000-to-600000-",
"pagename_nl":"Eigendom-aan-de-Costa-Blanca-van-500000-tot-600000-euro-",
"pagename_fr":"Propriete-a-Costa-Blanca-de-500000-euro-a-600000-euro-",
"pagename_de":"costa-blanca-Immobilien-von-500000-bis-600000-"
},
{
"rubrun":"6-7",
"query":"Select * FROM mghprops WHERE blndisplay = 1 AND blnrental = 0 AND intprice >= 601000  AND intprice <= 700000 ORDER BY intprice ASC",
"EN":{
"description":"Apartments, townhouses and Spanish villas priced between &euro;600,000 and &euro;700,000",
"keywords":"Costa Blanca homes, Villas, Apartments, Golf homes, Property South Costa Blanca, Spain",
"title":"Costa Blanca Property priced between &euro;600,000 and &euro;700,000",
"h1":"Property For Sale in Villamartin, Cabo Roig, Campoamor, Playa Flamenca Costa Blanca South priced between &euro;600,000 and &euro;700,000"},
"FR":{
"description":"Villas, appartements, maisons mitoyennes et fincas de 600 000 euros à 700 000 euros",
"keywords":"Maisons Costa Blanca, Villas, Appartements, Maisons sur le golf resort, Propriété Costa Blanca Sud, Espagne",
"title":"Propriété à Costa Blanca de 600 000 euros à 700 000 euros",
"h1":"Propriété à vendre à Villamartin, Cabo Roig, Campoamor, Playa Flamenca, Costa Blanca Sud de 600 000 euros à 700 000 euros"
},
"DE":{
"description":"Ferienwohnungen, Stadth&auml;user und spanische villas zwischen &euro;600,000 und &euro; 700,000 preislich",
"keywords":"Costa Blanca H&auml;user, Villas, Ferienwohnungen, Golf H&auml;user, Immobilien Costa Blanca S&uuml;d, Spanien",
"title":"Costa Blanca Immobilien priced zwischen &euro;600,000 und &euro; 700,000",
"h1":"Immobilien zu verkaufen in Villamartin, Cabo Roig, Campoamor, Playa Flamenca Costa Blanca S&uuml;d zwischen &euro;600,000 und &euro; 700,000 preislich"
},
"NL":{
"description":"Appartementen, geschakelde woningen en Spaanse villa's van 600.000 euro tot 700.000 euro",
"keywords":"Costa Blanca homes, Villas, Apartments, Golf homes, Property South Costa Blanca, Spain",
"title":"Eigendom aan de Costa Blanca van 600.000 euro tot 700.000 euro",
"h1":"Eigendom te koop in Villamartin, Cabo Roig, Campoamor, Playa Flamenca, Costa Blanca Zuid van &euro;600.000 tot &euro;700.000"
},
"pagename_en":"costa-blanca-property-from-600000-to-700000-",
"pagename_nl":"Eigendom-aan-de-Costa-Blanca-van-600000-tot-700000-euro-",
"pagename_fr":"Propriete-a-Costa-Blanca-de-600000-euro-a-700000-euro-",
"pagename_de":"costa-blanca-Immobilien-von-600000-bis-700000-"
},
{
"rubrun":"7-8",
"query":"Select * FROM mghprops WHERE blndisplay = 1 AND blnrental = 0 AND intprice >= 701000  AND intprice <= 800000 ORDER BY intprice ASC",
"EN":{
"description":"Apartments, townhouses and Spanish villas priced between &euro;700,000 and &euro;800,000",
"keywords":"Comfortable Costa Blanca homes, Villas, Apartments, Golf homes, Property South Costa Blanca, Spain",
"title":"Costa Blanca Property priced between &euro;700,000 and &euro;800,000",
"h1":"Property For Sale in Villamartin, Cabo Roig, Campoamor, Playa Flamenca Costa Blanca South priced between &euro;700,000 and &euro;800,000"},
"FR":{
"description":"Villas, appartements, maisons mitoyennes et fincas de 700 000 euros à 800 000 euros",
"keywords":"Maisons confortables Costa Blanca, villas, appartements, maisons sur le golf resort, propriété Costa Blanca Sud, Espagne",
"title":"Propriété à Costa Blanca de 700 000 euros à 800 000 euros",
"h1":"Propriété à vendre à Villamartin, Cabo Roig, Campoamor, Playa Flamenca, Costa Blanca Sud de 700 000 euros à 800 000 euros",
},
"DE":{
"description":"Ferienwohnungen, Stadth&auml;user und spanische villas zwischen &euro;700,000 und &euro; 800,000 preislich",
"keywords":"komfortabel Costa Blanca H&auml;user, Villas, Ferienwohnungen, Golf H&auml;user, Immobilien Costa Blanca S&uuml;d, Spanien",
"title":"Costa Blanca Immobilien priced zwischen &euro;700,000 und &euro; 800,000",
"h1":"Immobilien zu verkaufen in Villamartin, Cabo Roig, Campoamor, Playa Flamenca Costa Blanca S&uuml;d zwischen &euro;700,000 und &euro; 800,000 preislich"
},
"NL":{
"description":"Appartementen, geschakelde woningen en Spaanse villa's van &euro;700.000 tot &euro;800.000",
"keywords":"Comfortabele huizen Costa Blanca, villa's, appartementen, huizen aan de golf, eigendommen Costa Blanca Zuid, Spanje",
"title":"Eigendom aan de Costa Blanca van 700.000 euro tot 800.000 euro",
"h1":"Eigendom te koop in Villamartin, Cabo Roig, Campoamor, Playa Flamenca, Costa Blanca Zuid van &euro;700.000 tot &euro;800.000"
},
"pagename_en":"costa-blanca-property-from-700000-to-800000-",
"pagename_nl":"Eigendom-aan-de-Costa-Blanca-van-700000-tot-800000-euro-",
"pagename_fr":"Propriete-a-Costa-Blanca-de-700000-euro-a-800000-euro-",
"pagename_de":"costa-blanca-Immobilien-von-700000-bis-800000-"
},
{
"rubrun":"8-9",
"query":"Select * FROM mghprops WHERE blndisplay = 1 AND blnrental = 0 AND intprice >= 801000  AND intprice <= 900000 ORDER BY intprice ASC",
"EN":{
"description":"Apartments, townhouses and Spanish villas priced between &euro;800,000 and &euro;900,000",
"keywords":"Luxurious Costa Blanca homes, Villas, Apartments, Golf homes, Property South Costa Blanca, Spain",
"title":"Costa Blanca Property priced between &euro;800,000 and &euro;900,000",
"h1":"Property For Sale in Villamartin, Cabo Roig, Campoamor, Playa Flamenca Costa Blanca South priced between &euro;800,000 and &euro;900,000"},
"FR":{
"description":"Villas, appartements, maisons mitoyennes et fincas de 800 000 euros à 900 000 euros",
"keywords":"Maisons de luxe Costa Blanca, villas, appartements, maisons sur le golf resort, propriété Costa Blanca Sud, Espagne",
"title":"Propriété à Costa Blanca de 800 000 euros à 900 000 euros",
"h1":"Propriété à vendre à Villamartin, Cabo Roig, Campoamor, Playa Flamenca, Costa Blanca Sud de 800 000 euros à 900 000 euros"
},
"DE":{
"description":"Ferienwohnungen, Stadth&auml;user und spanische villas zwischen &euro;800,000 und &euro; 900,000 preislich",
"keywords":"Luxus Costa Blanca H&auml;user, Villas, Ferienwohnungen, Golf H&auml;user, Immobilien Costa Blanca S&uuml;d, Spanien",
"title":"Costa Blanca Immobilien priced zwischen &euro;800,000 und &euro; 900,000",
"h1":"Immobilien zu verkaufen in Villamartin, Cabo Roig, Campoamor, Playa Flamenca Costa Blanca S&uuml;d zwischen &euro;800,000 und &euro; 900,000 preislich"
},
"NL":{
"description":"Appartementen, geschakelde woningen en Spaanse villa's van 800,000 euro tot 900,000 euro",
"keywords":"Luxueuze huizen Costa Blanca, villa's, appartementen, huizen aan de golf, eigendommen Costa Blanca Zuid, Spanje",
"title":"Eigendom aan de Costa Blanca van 800.000 euro tot 900.000 euro",
"h1":"Eigendom te koop in Villamartin, Cabo Roig, Campoamor, Playa Flamenca, Costa Blanca Zuid van &euro;800.000 tot &euro;900.000"
},
"pagename_en":"costa-blanca-property-from-800000-to-900000-",
"pagename_nl":"Eigendom-aan-de-Costa-Blanca-van-800000-tot-900000-euro-",
"pagename_fr":"Propriete-a-Costa-Blanca-de-800000-euro-a-900000-euro-",
"pagename_de":"costa-blanca-Immobilien-von-800000-bis-900000-"
},
{
"rubrun":"9-10",
"query":"Select * FROM mghprops WHERE blndisplay = 1 AND blnrental = 0 AND intprice > 900000 ORDER BY intprice ASC",
"EN":{
"description":"Apartments, townhouses and Spanish villas priced over &euro;900,000",
"keywords":"Distinctive Costa Blanca homes, Villas, Apartments, Golf homes, Property South Costa Blanca, Spain",
"title":"Destinctive Costa Blanca Property priced over &euro;900,000",
"h1":"Property For Sale in Villamartin, Cabo Roig, Campoamor, Playa Flamenca Costa Blanca South priced over &euro;900,000"},
"FR":{
"description":"Villas, appartements, maisons mitoyennes et fincas à partir de 900 000 euros",
"keywords":"Maisons uniques Costa Blanca, villas, appartements, maisons sur le golf resort, propriété Costa Blanca Sud, Espagne",
"title":"Propriétés uniques à Costa Blanca à partir de 900 000 euros",
"h1":"Propriété à vendre à Villamartin, Cabo Roig, Campoamor, Playa Flamenca, Costa Blanca Sud à partir de 900 000 euros"
},
"DE":{
"description":"Ferienwohnungen, Stadth&auml;user und spanische villas priced over &euro;900,000",
"keywords":"Unverwechselbar Costa Blanca H&auml;user, Villas, Ferienwohnungen, Golf H&auml;user, Immobilien Costa Blanca S&uuml;d, Spanien",
"title":"Unverwechselbar Costa Blanca Immobilien von &euro;900,000",
"h1":"Immobilien zu verkaufen in Villamartin, Cabo Roig, Campoamor, Playa Flamenca Costa Blanca S&uuml;d Preis mehr als&euro;900,000"
},
"NL":{
"description":"Appartementen, geschakelde woningen en Spaanse villa's vanaf 900.000 euro",
"keywords":"Unieke huizen Costa Blanca, villa's, appartementen, huizen aan de golf, eigendommen Costa Blanca Zuid, Spanje",
"title":"Unieke eigendommen aan de Costa Blanca vanaf 900.000 euro",
"h1":"Eigendom te koop in Villamartin, Cabo Roig, Campoamor, Playa Flamenca, en de Costa Blanca Zuid vanaf &euro;900.000"
},
"pagename_en":"costa-blanca-property-from-900000-",
"pagename_nl":"Eigendom-aan-de-Costa-Blanca-vanaf-900000-euro-",
"pagename_fr":"Propriete-a-Costa-Blanca-a-partir-de-900000-euro-",
"pagename_de":"costa-blanca-Immobilien-von-900000-"
},
{
"rubrun":"commercial",
"query":"Select * FROM mghprops WHERE blndisplay = 1 AND (strpropertytype IN ('Bar','Restaurant','Business','Commercial','Hotel')) ORDER BY intprice ASC",
"EN":{
"description":"Business and commercial property in South Costa Blanca Bars, Restaurants, Hotels",
"keywords":"Commercial property Costa Blanca, business property Costa Blanca, Bars, Restaurants, Hotels",
"title":"Commercial property Costa Blanca",
"h1":"Commercial property Costa Blanca South"},
"FR":{
"description":"Bâtiments commerciaux et bureaux à Costa Blanca Sud, cafés, restaurants, hôtels",
"keywords":"bâtiments commerciaux Costa Blanca, bureaux Costa Blanca, cafés, restaurants, hôtels",
"title":"Bâtiments commerciaux à Costa Blanca ",
"h1":"Bâtiments commerciaux Costa Blanca Sud"
},
"DE":{
"description":"Business and commercial Immobilien in Costa Blanca S&uuml;d Bars, Restaurants, Hotels",
"keywords":"Commercial Immobilien Costa Blanca, Gesch&auml;ft zum Verkauf Costa Blanca, Bars, Restaurants, Hotels",
"title":"Gewerbeimmobilien Costa Blanca",
"h1":"Gewerbeimmobilien Costa Blanca S&uuml;d"
},
"NL":{
"description":"Commerciele panden en kantoren in Costa Blanca Zuid, cafes, restaurants, hotels",
"keywords":"commerciele panden Costa Blanca, kantoren Costa Blanca, cafes, restaurants, hotels",
"title":"Commerci&euml;le panden aan de Costa Blanca",
"h1":"Commerci&euml;le panden Costa Blanca Zuid"
},
"pagename_en":"costa-blanca-commercial-property-",
"pagename_nl":"Commerciele-panden-Costa-Blanca-Zuid-",
"pagename_fr":"Batiments-commerciaux-Costa-Blanca-Sud-",
"pagename_de":"costa-blanca-Gewerbeimmobilien-"
},
{
"rubrun":"long-term-rental",
"query":"Select * FROM mghprops WHERE blndisplay = 1 AND blnrental = 1 AND strFrequency = 'month' ORDER BY intprice ASC",
"EN":{
"description":"Property for long term rent in Costa Blanca South",
"keywords":"Costa Blanca lettings,Long term let, long term rental",
"title":"Costa Blanca Homes for long term rental",
"h1":"Long Term Rental Property Costa Blanca South"},
"FR":{
"description":"Propriété à louer pour long terme à Costa Blanca Sud",
"keywords":"louer Costa Blanca, louer pour long terme, louer long terme ",
"title":"Maisons à Costa Blanca à louer pour long terme",
"h1":"Propriété à louer pour long terme Costa Blanca Sud"
},
"DE":{
"description":"Langfristige Vermietungen in Costa Blanca S&uuml;d",
"keywords":"Costa Blanca Vermietung, Langzeitmiete",
"title":"Costa Blanca Immobilien zur Langzeitmiete",
"h1":"Immobilien zur Langzeitmiete Costa Blanca S&uuml;d"
},
"NL":{
"description":"Eigendom te huur voor lange termijn in Costa Blanca Zuid",
"keywords":"verhuur Costa Blanca, verhuur voor lange termijn, verhuur lange termijn",
"title":"Huizen aan de Costa Blanca voor lange-termijnverhuur",
"h1":"Eigendom te huur voor lange termijn Costa Blanca Zuid"
},
"pagename_en":"costa-blanca-long-term-rental-property-",
"pagename_nl":"Eigendom-te-huur-voor-lange-termijn-costa-blanca-zuid-",
"pagename_fr":"Propriete-a-louer-pour-long-terme-Costa-Blanca-Sud-",
"pagename_de":"costa-blanca-Langfristige-Vermietungen-"
},
{
"rubrun":"holiday-rentals",
"query":"Select * FROM mghprops WHERE blndisplay = 1 AND blnrental = 1 AND strFrequency = 'week' ORDER BY intprice ASC",
"EN":{
"description":"Holiday property for rent in Costa Blanca South",
"keywords":"Costa Blanca lettings,holiday let, Holiday rental",
"title":"Costa Blanca Holiday Rental Property",
"h1":"Holiday Rental Property Costa Blanca South"},
"FR":{
"description":"Maisons de vacances à louer à Costa Blanca Sud",
"keywords":"Louer Costa Blanca, louer pour vacances, louer vacances",
"title":"Maisons de vacances à louer à Costa Blanca",
"h1":"Maisons de vacances à louer Costa Blanca Sud"
},
"DE":{
"description":"Zu Vermietende Ferienunterk&auml;Nfte in Costa Blanca S&uuml;d",
"keywords":"Costa Blanca Zu Vermietende Ferienunterk&auml;nfte",
"title":"Costa Blanca Immobilien Zu Vermietende Ferienunterk&auml;nfte",
"h1":"Immobilien Zu Vermietende Ferienunterk&auml;Nfte Costa Blanca S&uuml;d"
},
"NL":{
"description":"Vakantieverhuur Costa Blanca Zuid",
"keywords":"Verhuur Costa Blanca, vakantieverhuur, vakantieverhuur",
"title":"Vakantieverhuur aan de Costa Blanca",
"h1":"Vakantieverhuur Costa Blanca Zuid"
},
"pagename_en":"costa-blanca-holiday-rental-property-",
"pagename_nl":"Vakantieverhuur-costa-blanca-zuid-",
"pagename_fr":"Maisons-de-vacances-a-louer-Costa-Blanca-Sud-",
"pagename_de":"costa-blanca-FerienunterkuNfte-"
},
{
"rubrun":"key-ready",
"query":"Select * FROM mghprops WHERE blndisplay = 1 AND blnoffplan = 1 ORDER BY intprice ASC",
"EN":{
"description":"Property in Costa Blanca South. Key ready and offplan at beach and inland ",
"keywords":"Key ready apartments, key ready townhouses, key ready villas, Costa Blanca South",
"title":"Key ready homes Costa Blanca South",
"h1":"Key Ready property Villamartin, Cabo Roig, Campoamor, Playa Flamenca Costa Blanca South"},
"FR":{
"description":"Propriété Costa Blanca Sud. Clé sur porte et nouvelles constructions sur la plage et à l' intérieur",
"keywords":"Appartements clé sur porte, maisons mitoyennes clé sur porte, villas clé sur porte, Costa Blanca Sud",
"title":"Maisons clé sur porte Costa Blanca Sud",
"h1":"Propriétés clé sur porte à Villamartin, Cabo Roig, Campoamor, Playa Flamenca, Costa Blanca Sud"
},
"DE":{
"description":"neue H&auml;user zum Verkauf in Costa Blanca S&uuml;d.",
"keywords":"neue Ferienwohnungen, neue Stadth&auml;user, neue villas, Costa Blanca S&uuml;d",
"title":"neue H&auml;user zum Verkauf in Costa Blanca S&uuml;d",
"h1":"neue H&auml;user Villamartin, Cabo Roig, Campoamor, Playa Flamenca Costa Blanca S&uuml;d"
},
"NL":{
"description":"Eigendom in Costa Blanca Zuid. Sleutel op de deur en nieuwbouw aan het strand en in het binnenland",
"keywords":"Sleutel op de deur-appartementen, sleutel op de deur geschakelde woningen, sleutel op de deur villa's, Costa Blanca Zuid",
"title":"Sleutel op de deur-huizen Costa Blanca Zuid",
"h1":"Sleutel op de deur-eigendommen in Villamartin, Cabo Roig, Campoamor, Playa Flamenca, Costa Blanca Zuid"
},
"pagename_en":"key-ready-homes-costa-blanca-south-",
"pagename_nl":"nieuwbouw-costa-blanca-zuid-",
"pagename_fr":"nouvelles-constructions-Costa-Blanca-Sud-",
"pagename_de":"neue-Hauser-costa-blanca-sud-"
},
{
"rubrun":"penthouse",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnpenthouse = 1 ORDER BY intprice ASC",
"EN":{
"description":"Penthouse apartments and penthouse duplexes in Costa Blanca South",
"keywords":"penthouse apartments,Costa Blanca South, Spain",
"title":"Penthouse apartments South Costa Blanca",
"h1":"Penthouse apartments for sale South Costa Blanca"},
"FR":{
"description":"Appartements à deux étages à Costa Blanca Sud",
"keywords":"appartements à deux étages, Costa Blanca Sud, Espagne, appartements deux étages, Costa Blanca Sud, Espagne",
"title":"Appartements à deux étages à Costa Blanca Sud",
"h1":"Appartements à deux étages à vendre à Costa Blanca Sud"
},
"DE":{
"description":"Penthouse Ferienwohnungen und penthouse duplex in Costa Blanca S&uuml;d",
"keywords":"penthouse Ferienwohnungen,Costa Blanca S&uuml;d, Spanien",
"title":"Penthouse Ferienwohnungen Costa Blanca S&uuml;d",
"h1":"Penthouse Ferienwohnungen zu verkaufen Costa Blanca S&uuml;d"
},
"NL":{
"description":"Penthouse appartementen en penthouse duplexen in Costa Blanca Zuid",
"keywords":"penthouse appartementen, Costa Blanca Zuid, Spanje",
"title":"Penthouse appartementen in Costa Blanca Zuid",
"h1":"Penthouse appartementen te koop in Costa Blanca Zuid"
},
"pagename_en":"penthouse-apartments-south-costa-blanca-",
"pagename_nl":"Penthouse-dakappartement-costa-blanca-zuid-",
"pagename_fr":"Appartements-a-deux-etages-Costa-Blanca-Sud-",
"pagename_de":"penthouse-Ferienwohnungen-costa-blanca-sud-"
},
{
"rubrun":"beach",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnbeach = 1 ORDER BY intprice ASC",
"EN":{
"description":"Property for sale at the beach in Costa Blanca South",
"keywords":"beach apartments,beach townhouses, beach villas, Costa Blanca South, Spain",
"title":"Property near the beach South Costa Blanca",
"h1":"Beach Property For Sale - Costa Blanca South, Spain"},
"FR":{
"description":"Propriété à vendre sur la plage à Costa Blanca Sud",
"keywords":"appartements plage, maisons mitoyennes plage, villas plage, Costa Blanca Sud, Espagne.",
"title":"Propriété sur la plage, Costa Blanca Sud",
"h1":"Propriété à vendre sur la plage, Costa Blanca Sud, Espagne"
},
"DE":{
"description":"Immobilien zu verkaufen at the beach in Costa Blanca S&uuml;d",
"keywords":"Strand Ferienwohnungen,Strand Stadth&auml;user, Strand villas, Costa Blanca S&uuml;d, Spanien",
"title":"Strand Immobilien Costa Blanca S&uuml;d",
"h1":"Ferienwohnungen, Stadth&auml;user, Villas N&auml;he zum Strand - Costa Blanca S&uuml;d, Spanien"
},
"NL":{
"description":"Eigendom te koop aan het strand in Costa Blanca Zuid",
"keywords":"appartementen strand, geschakelde woningen strand, villa's strand, Costa Blanca Zuid, Spanje",
"title":"Eigendom aan het strand, Costa Blanca Zuid",
"h1":"Eigendom te koop aan het strand, Costa Blanca Zuid, Spanje"
},
"pagename_en":"beach-property-south-costa-blanca-",
"pagename_nl":"Eigendom-aan-het-strand-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-sur-la-plage-Costa-Blanca-Sud-",
"pagename_de":"Strand-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"golf",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blngolf = 1 ORDER BY intprice ASC",
"EN":{
"description":"Golf property for sale in Costa Blanca South",
"keywords":"golf apartments,golf townhouses, golf villas, Costa Blanca South, Spain",
"title":"Property near to or on the golf course South Costa Blanca",
"h1":"Golf Property For Sale - Costa Blanca South, Spain"},
"FR":{
"description":"Propriété à vendre sur le golf resort à Costa Blanca Sud",
"keywords":"appartements golf resort, maisons mitoyennes golf resort, villas golf resort, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre sur le golf resort à Costa Blanca Sud",
"h1":"Propriété à vendre sur le golf resort - Costa Blanca Sud, Espagne"
},
"DE":{
"description":"Golf Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"golf Ferienwohnungen,golf Stadth&auml;user, golf villas, Costa Blanca S&uuml;d, Spanien",
"title":"Immobilien in der N&auml;he des Golfplatzes auf dem Golfplatz Costa Blanca S&uuml;d",
"h1":"Golf Ferienwohnungen, Golf Stadth&auml;user, Golf Villas - Costa Blanca S&uuml;d, Spanien"
},
"NL":{
"description":"Eigendom te koop aan de golf in Costa Blanca Zuid",
"keywords":"appartementen golf, geschakelde woningen golf, villa's golf, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop aan de golf in Costa Blanca Zuid",
"h1":"Eigendom te koop aan de golf - Costa Blanca Zuid, Spanje"
},
"pagename_en":"golf-property-south-costa-blanca-",
"pagename_nl":"Eigendom-aan-de-golf-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-sur-le-golf-resort-Costa-Blanca-Sud-",
"pagename_de":"golf-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"apartment",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND strpropertytype = 'Apartment' ORDER BY intprice ASC",
"EN":{
"description":"Apartments for sale Costa Blanca South",
"keywords":"spanish apartment, costa blanca apartment, apartment spain, beach apartment, golf apartment, luxury apartment, penthouse apartment",
"title":"Apartments for sale South Costa Blanca",
"h1":"Apartments Villamartin, Cabo Roig, Campoamor, Playa Flamenca Costa Blanca South"},
"FR":{
"description":"Appartements à vendre à Costa Blanca Sud",
"keywords":"appartement espagnol, appartement Costa Blanca Sud, appartement Espagne, appartement plage, appartement golf resort appartement de luxe",
"title":"Appartements à vendre Costa Blanca Sud",
"h1":"Appartements à Villamartin, Cabo Roig, Campoamor, Playa Flamenca, Costa Blanca Sud"
},
"DE":{
"description":"Ferienwohnungen zu verkaufen Costa Blanca S&uuml;d",
"keywords":"spanische Wohnung, wohnung costa blanca, wohnung Spanien, Strand-wohnung, golf-Wohnung, Luxus-Wohnung, Penthouse-Wohnung",
"title":"Ferienwohnungen zu verkaufen Costa Blanca S&uuml;d",
"h1":"Wohnungen Villamartin, Cabo Roig, Campoamor, Playa Flamenca Costa Blanca S&uuml;d"
},
"NL":{
"description":"Appartementen te koop aan de Costa Blanca Zuid",
"keywords":"Spaans appartement, appartement Costa Blanca Zuid, appartement Spanje, appartement strand, appartement golf, luxueuze appartement",
"title":"Appartementen te koop Costa Blanca Zuid",
"h1":"Appartementen in Villamartin, Cabo Roig, Campoamor, Playa Flamenca, Costa Blanca Zuid"
},
"pagename_en":"apartments-for-sale-costa-blanca-south-",
"pagename_nl":"Appartement-te-koop-costa-blanca-zuid-",
"pagename_fr":"Appartements-a-vendre-Costa-Blanca-Sud-",
"pagename_de":"Ferienwohnungen-zu-verkaufen-costa-blanca-sud-"
},
{
"rubrun":"townhouse",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND strpropertytype = 'Townhouse' ORDER BY intprice ASC",
"EN":{
"description":"Townhouses for sale Costa Blanca South",
"keywords":"spanish townhouse, costa blanca townhouse, townhouses spain, beach townhouse, golf townhouse, luxury townhouse",
"title":"Townhouses for sale South Costa Blanca",
"h1":"Townhouses Villamartin, Cabo Roig, Campoamor, Playa Flamenca Costa Blanca South"},
"FR":{
"description":"Maisons mitoyennes à vendre à Costa Blanca Sud",
"keywords":"maison mitoyenne espagnole, maison mitoyenne Costa Blanca, maison mitoyenne Espagne, maison mitoyenne plage, maison mitoyenne golf resort, maison mitoyenne de luxe",
"title":"Maisons mitoyennes à vendre Costa Blanca Sud",
"h1":"Maisons mitoyennes à Villamartin, Cabo Roig, Campoamor, Playa Flamenca, Costa Blanca Sud"
},
"DE":{
"description":"Reihenh&auml;user zu verkaufen Costa Blanca S&uuml;d",
"keywords":"spanische Reihenh&auml;user, costa blanca Reihenh&auml;user, Reihenh&auml;user Spanien, Strand Stadthaus, golf Reihenh&auml;user, luxury Reihenh&auml;user",
"title":"Reihenh&auml;user zu verkaufen Costa Blanca S&uuml;d",
"h1":"Reihenh&auml;user Villamartin, Cabo Roig, Campoamor, Playa Flamenca Costa Blanca S&uuml;d"
},
"NL":{
"description":"Geschakelde woningen te koop Costa Blanca Zuid",
"keywords":"geschakelde woning Spanje,  geschakelde woning Costa Blanca, geschakelde woningen Spanje, geschakelde woning strand, geschakelde woning golf, luxueuze geschakelde woning",
"title":"Geschakelde woningen te koop Costa Blanca Zuid",
"h1":"Geschakelde woningen in Villamartin, Cabo Roig, Campoamor, Playa Flamenca, Costa Blanca Zuid"
},
"pagename_en":"townhouses-for-sale-costa-blanca-south-",
"pagename_nl":"Geschakelde-woningen-Costa-Blanca-Zuid-",
"pagename_fr":"Maisons-mitoyennes-Costa-Blanca-Sud-",
"pagename_de":"Stadthauser-zu-verkaufen-costa-blanca-sud-"
},
{
"rubrun":"quadhouse",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND strpropertytype = 'Quadhouse' ORDER BY intprice ASC",
"EN":{
"description":"Quadhouses for sale Costa Blanca South",
"keywords":"spanish quadhouse, costa blanca quadhouse, quadhouses spain, beach quadhouse, golf quadhouse, spacious quadhouse",
"title":"Quadhouses for sale South Costa Blanca",
"h1":"Quadhouses Villamartin, Cabo Roig, Campoamor, Playa Flamenca Costa Blanca South"},
"FR":{
"description":"Maisons mitoyennes (quatre sous un même toit) à vendre à Costa Blanca Sud",
"keywords":"Maison mitoyenne (quatre sous un même toit) espagnole,  maison mitoyenne (quatre sous un même toit) Costa Blanca, maison mitoyenne (quatre sous un même toit) Espagne, maison mitoyenne (quatre sous un même toit) plage, maison mitoyenne (quatre sous un même toit) golf resort, maison mitoyenne (quatre sous un même toit) spacieuse",
"title":"Maisons mitoyennes (quatre sous un même toit) à vendre Costa Blanca Sud",
"h1":"Maisons mitoyennes (quatre sous un même toit) à Villamartin, Cabo Roig, Campoamor, Playa Flamenca, Costa Blanca Sud"
},
"DE":{
"description":"quadHaus zu verkaufen Costa Blanca S&uuml;d",
"keywords":"spanische quadHaus, costa blanca quadHaus, quadHaus Spanien, Strand quadHaus, golf quadHaus, gro&szlig;z&uuml;gig quadHaus",
"title":"Quadhaus zu verkaufen Costa Blanca S&uuml;d",
"h1":"Quadhaus Villamartin, Cabo Roig, Campoamor, Playa Flamenca Costa Blanca Sud"
},
"NL":{
"description":"Kwadranthuizen (4 onder een dak) te koop Costa Blanca Zuid",
"keywords":"Kwadranthuis (4 onder een dak) Spanje, kwadranthuis (4 onder een dak) Costa Blanca, kwadranthuizen (4 onder een dak) Spanje,kwadranthuis (4 onder een dak) strand, kwadranthuis (4 onder een dak) golf, ruim kwadranthuis (4 onder een dak)",
"title":"Kwadranthuizen (4 onder een dak) te koop Costa Blanca Zuid.",
"h1":"Kwadranthuizen (4 onder een dak) in Villamartin, Cabo Roig, Campoamor, Playa Flamenca, Costa Blanca Zuid"
},
"pagename_en":"quadhouses-for-sale-costa-blanca-south-",
"pagename_nl":"Kwadranthuizen-Costa-Blanca-Zuid-",
"pagename_fr":"Maisons-mitoyennes-quatre-Costa-Blanca-Sud-",
"pagename_de":"quadhaus-zu-verkaufen-costa-blanca-sud-"
},
{
"rubrun":"semidetached-villa",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND strpropertytype = 'Semidetached Villa' ORDER BY intprice ASC",
"EN":{
"description":"Semidetached Villas for sale Costa Blanca South",
"keywords":"spanish semidetached villa, costa blanca semidetached villa, semidetached villas spain, beach semidetached villa, golf semidetached villa, spacious semidetached villa",
"title":"Semidetached Villas for sale South Costa Blanca",
"h1":"Semidetached Villas Villamartin, Cabo Roig, Campoamor, Playa Flamenca Costa Blanca South"},
"FR":{
"description":"Villas jumelées à vendre à Costa Blanca Sud",
"keywords":"villa jumelée espagnole, villa jumelée Costa Blanca, villa jumelée Espagne, villa jumelée plage, villa jumelée golf resort, villa jumelée spacieuse",
"title":"Villas jumelées à vendre Costa Blanca Sud",
"h1":"Villas jumelées à Villamartin, Cabo Roig, Campoamor, Playa Flamenca, Costa Blanca Sud"
},
"DE":{
"description":"Doppelhaus Villa zu verkaufen Costa Blanca S&uuml;d",
"keywords":"spanische Doppelhaus Villa, costa blanca Doppelhaus Villa, Doppelhaus Villa Spanien, Strand Doppelhaus Villa, golf Doppelhaus Villa, gro&szlig;z&uuml;gig Doppelhaus Villa",
"title":"Doppelhaus Villa zu verkaufen Costa Blanca S&uuml;d",
"h1":"Doppelhaus Villa Villamartin, Cabo Roig, Campoamor, Playa Flamenca Costa Blanca S&uuml;d"
},
"NL":{
"description":"Half-vrijstaande villa's te koop Costa Blanca Zuid",
"keywords":"Half-vrijstaande villa's Spanje, half-vrijstaande villa's Costa Blanca. Half-vrijstaande villa's Spanje, half-vrijstaande villa aan het strand, half-vrijstaande villa aan de golf, ruimehalf-vrijstaande villa",
"title":"Half-vrijstaande villa's te koop Costa Blanca Zuid",
"h1":"Half-vrijstaande villa's In Villamartin, Cabo Roig, Campoamor, Playa Flamenca, Costa Blanca Zuid"
},
"pagename_en":"semidetached-villas-for-sale-costa-blanca-south-",
"pagename_nl":"Half-vrijstaande-villas-Costa-Blanca-Zuid-",
"pagename_fr":"Villas-jumelees-Costa-Blanca-Sud-",
"pagename_de":"Doppelhaus-villa-zu-verkaufen-costa-blanca-sud-"
},
{
"rubrun":"villa",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND (strpropertytype = 'Villa' OR strpropertytype = 'Detached Villa') ORDER BY intprice ASC",
"EN":{
"description":"Villas for sale Costa Blanca South",
"keywords":"spanish villa, costa blanca villa, villas spain, beach villa, golf villa, spacious villa",
"title":"Villas for sale South Costa Blanca",
"h1":"Villas Villamartin, Cabo Roig, Campoamor, Playa Flamenca Costa Blanca South"},
"FR":{
"description":"Villas à vendre à Costa Blanca Sud",
"keywords":"villa espagnole, villa Costa Blanca, villa Espagne, villa plage, villa golf resort, villa spacieuse",
"title":"Villas à vendre Costa Blanca Sud",
"h1":"Villas à Villamartin, Cabo Roig, Campoamor, Playa Flamenca, Costa Blanca Sud"
},
"DE":{
"description":"Villas zu verkaufen Costa Blanca S&uuml;d",
"keywords":"spanische villa, costa blanca villa, villas Spanien, Strand villa, golf villa, gro&szlig;z&uuml;gig villa",
"title":"Villas zu verkaufen Costa Blanca S&uuml;d",
"h1":"Villas Villamartin, Cabo Roig, Campoamor, Playa Flamenca Costa Blanca S&uuml;d"
},
"NL":{
"description":"Villa's te koop Costa Blanca Zuid",
"keywords":"Spaanse villa, villa Costa Blanca, villa Spanje, villa aan de zee, villa aan de golf, ruime villa",
"title":"Villa's te koop Costa Blanca Zuid",
"h1":"Villa's Villamartin, Cabo roig, Campoamor, Playa Flamenca, Costa Blanca Zuid"
},
"pagename_en":"villas-for-sale-costa-blanca-south-",
"pagename_nl":"Villas-Costa-Blanca-Zuid-",
"pagename_fr":"Villas-Costa-Blanca-Sud-",
"pagename_de":"villas-zu-verkaufen-costa-blanca-south-"
},
{
"rubrun":"finca",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnfinca = 1 ORDER BY intprice ASC",
"EN":{
"description":"Fincas and country homes for sale Costa Blanca South",
"keywords":"spanish fincas and country homes, costa blanca fincas and country homes, fincas and country homes spain, spacious fincas and country homes",
"title":"Fincas and Country Homes for sale South Costa Blanca",
"h1":"Fincas and Country Homes Costa Blanca South"},
"FR":{
"description":"Fincas et maisons de campagne à vendre à Costa Blanca Sud",
"keywords":"Fincas et maisons de campagne espagnoles, fincas et maisons de campagne Costa Blanca, fincas et maisons de campagne Espagne, fincas et maisons de campagne spacieuses",
"title":"Fincas et maisons de campagne à vendre Costa Blanca Sud",
"h1":"Fincas et maisons de campagne Costa Blanca Sud"
},
"DE":{
"description":"L&auml;ndliche Landh&auml;user zu verkaufen Costa Blanca S&uuml;d",
"keywords":"spanische L&auml;ndliche Landh&auml;user, costa blanca L&auml;ndliche Landh&auml;user, L&auml;ndliche Landh&auml;user Spanien, gro&szlig;z&uuml;gig L&auml;ndliche Landh&auml;user",
"title":"L&auml;ndliche Landh&auml;user zu verkaufen Costa Blanca S&uuml;d",
"h1":"L&auml;ndliche Landh&auml;user Costa Blanca S&uuml;d"
},
"NL":{
"description":"Finca's en landhuizen te koop Costa Blanca Zuid",
"keywords":"Spaanse finca's en landhuizen, finca's en landhuizen Costa Blanca, finca's en landhuizen Spanje, ruime finca's en landhuizen",
"title":"Finca's en landhuizen te koop Costa Blanca Zuid",
"h1":"Finca's en landhuizen Costa Blanca Zuid"
},
"pagename_en":"fincas-and-country-homes-for-sale-costa-blanca-south-",
"pagename_nl":"Fincas-en-landhuizen-Costa-Blanca-Zuid-",
"pagename_fr":"Fincas-et-maisons-de-campagne-Costa-Blanca-Sud-",
"pagename_de":"Landliche-Landhauser-zu-verkaufen-costa-blanca-south-"
},
{
"rubrun":"luxury",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND blnluxury = 1 ORDER BY intprice ASC",
"EN":{
"description":"Luxury property for sale in Costa Blanca South",
"keywords":"luxury apartments,luxury townhouses, luxury villas, Costa Blanca South, Spain",
"title":"Luxury property for sale South Costa Blanca",
"h1":"Luxury property for sale Villamartin, Cabo Roig, Campoamor, Playa Flamenca Costa Blanca South"},
"FR":{
"description":"Propriété de luxe à vendre à Costa Blanca Sud",
"keywords":"appartements de luxe, maisons mitoyennes de luxe, villas de luxe, Costa Blanca Sud, Espagne",
"title":"Propriété de luxe à vendre Costa Blanca Sud",
"h1":"Propriété de luxe à vendre à Villamartin, Cabo Roig, Campoamor, Playa Flamenca, Costa Blanca Sud"
},
"DE":{
"description":"Luxus Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"luxury Ferienwohnungen,luxury Stadth&auml;user, luxury villas, Costa Blanca S&uuml;d, Spanien",
"title":"Luxus Immobilien zu verkaufen Costa Blanca S&uuml;d",
"h1":"Luxus Immobilien zu verkaufen Villamartin, Cabo Roig, Campoamor, Playa Flamenca Costa Blanca S&uuml;d"
},
"NL":{
"description":"Luxe-eigendom te koop in Costa Blanca Zuid",
"keywords":"luxe-appartementen, luxueuze geschakelde woningen, luxueuze villa's, Costa Blanca Zuid, Spanje",
"title":"Luxe-eigendom te koop Costa Blanca Zuid",
"h1":"Luxe-eigendom te koop in Villamartin, Cabo roig, Campoamor, Playa Flamenca, Costa Blanca Zuid"
},
"pagename_en":"luxury-property-south-costa-blanca-",
"pagename_nl":"Luxe-eigendom-te-koop-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-de-luxe-a-vendre-Costa-Blanca-Sud-",
"pagename_de":"Luxus-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"orihuela-costa",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strtown = 'Orihuela Costa' ORDER BY intprice ASC",
"EN":{
"description":"Orihuela Costa property for sale in Costa Blanca South",
"keywords":"Orihuela Costa apartments,Orihuela Costa townhouses, Orihuela Costa villas, Costa Blanca South, Spain",
"title":"Orihuela Costa property for sale South Costa Blanca",
"h1":"Property for sale Orihuela Costa, Villamartin, Cabo Roig, Campoamor, Playa Flamenca"},
"FR":{
"description":"Propriété à vendre à Orihuela Costa, Costa Blanca Sud",
"keywords":"Appartements Orihuela Costa, maisons mitoyennes Orihuela Costa, villas Orihuela Costa, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre Orihuela Costa, Costa Blanca Sud",
"h1":"Propriété à vendre à Orihuela Costa, Villamartin, Cabo Roig, Campoamor, Playa Flamenca"
},
"DE":{
"description":"Orihuela Costa Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"Orihuela Costa Ferienwohnungen,Orihuela Costa Stadth&auml;user, Orihuela Costa villas, Costa Blanca S&uuml;d, Spanien",
"title":"Orihuela Costa Immobilien zu verkaufen Costa Blanca S&uuml;d",
"h1":"Immobilien zu verkaufen Orihuela Costa, Villamartin, Cabo Roig, Campoamor, Playa Flamenca"
},
"NL":{
"description":"Eigendom te koop in Orihuela Costa, Costa Blanca Zuid",
"keywords":"Appartementen Orihuela Costa, geschakelde woningen Orihuela Costa, villa's Orihuela Costa, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop Orihuela Costa, Costa Blanca Zuid",
"h1":"Eigendom te koop Orihuela Costa, Villamartin, Cabo Roig, Campoamor, Playa Flamenca"
},
"pagename_en":"orihuela-costa-property-south-costa-blanca-",
"pagename_nl":"Eigendom-te-koop-in-Orihuela-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-a-vendre-a-Orihuela-Costa-Costa-Blanca-Sud-",
"pagename_de":"orihuela-costa-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"villamartin",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strlocation_detail IN('Villamartin','Villamartin Golf') ORDER BY intprice ASC",
"EN":{
"description":"Villamartin property for sale in Costa Blanca South",
"keywords":"Villamartin apartments, Villamartin townhouses, Villamartin villas, Costa Blanca South, Spain",
"title":"Villamartin property for sale South Costa Blanca",
"h1":"Villamartin Property For Sale"},
"FR":{
"description":"Propriété à vendre à Villamartin, Costa Blanca Sud",
"keywords":"Appartements Villamartin, maisons mitoyennes Villamartin, villas Villamartin, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre Villamartin, Costa Blanca Sud",
"h1":"Propriété à vendre Villamartin"
},
"DE":{
"description":"Villamartin Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"Villamartin Ferienwohnungen, Villamartin Stadth&auml;user, Villamartin villas, Costa Blanca S&uuml;d, Spanien",
"title":"Villamartin Immobilien zu verkaufen Costa Blanca S&uuml;d",
"h1":"Villamartin Immobilien zu verkaufen"
},
"NL":{
"description":"Villamartin property for sale in Costa Blanca South",
"keywords":"Appartementen Villamartin, geschakelde woningen Villamartin, villa's Villamartin, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop Villamartin, Costa Blanca Zuid",
"h1":"Eigendom te koop Villamartin"
},
"pagename_en":"villamartin-property-south-costa-blanca-",
"pagename_nl":"Eigendom-te-koop-in-Villamartin-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-a-vendre-a-Villamartin-Costa-Blanca-Sud-",
"pagename_de":"villamartin-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"playa-flamenca",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strlocation_detail ='Playa Flamenca' ORDER BY intprice ASC",
"EN":{
"description":"Playa Flamenca property for sale in Costa Blanca South",
"keywords":"Playa Flamenca apartments, Playa Flamenca townhouses, Playa Flamenca villas, Costa Blanca South, Spain",
"title":"Playa Flamenca property for sale South Costa Blanca",
"h1":"Playa Flamenca Property For Sale"},
"FR":{
"description":"Propriété à vendre à Playa Flamenca, Costa Blanca Sud",
"keywords":"Appartements Playa Flamenca, maisons mitoyennes Playa Flamenca, villas Playa Flamenca, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre Playa Flamenca, Costa Blanca Sud",
"h1":"Propriété à vendre Playa Flamenca"
},
"DE":{
"description":"Playa Flamenca Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"Playa Flamenca Ferienwohnungen, Playa Flamenca Stadth&auml;user, Playa Flamenca villas, Costa Blanca S&uuml;d, Spanien",
"title":"Playa Flamenca Immobilien zu verkaufen Costa Blanca S&uuml;d",
"h1":"Playa Flamenca Immobilien zu verkaufen"
},
"NL":{
"description":"Eigendom te koop in Playa Flamenca, Costa Blanca Zuid",
"keywords":"Appartementen Playa Flamenca, geschakelde woningen Playa Flamenca, villa's Playa Flamenca, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop Playa Flamenca, Costa Blanca Zuid",
"h1":"Eigendom te koop Playa Flamenca"
},
"pagename_en":"playa-flamenca-property-south-costa-blanca-",
"pagename_nl":"Eigendom-te-koop-in-Playa-Flamenca-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-a-vendre-a-Playa-Flamenca-Costa-Blanca-Sud-",
"pagename_de":"playa-flamenca-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"cabo-roig",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strlocation_detail ='Cabo Roig' ORDER BY intprice ASC",
"EN":{
"description":"Cabo Roig property for sale in Costa Blanca South",
"keywords":"Cabo Roig apartments, Cabo Roig townhouses, Cabo Roig villas, Costa Blanca South, Spain",
"title":"Cabo Roig property for sale South Costa Blanca",
"h1":"Cabo Roig Property For Sale"},
"FR":{
"description":"Propriété à vendre à Cabo Roig, Costa Blanca Sud",
"keywords":"Appartements Cabo Roig, maisons mitoyennes Cabo Roig, villas Cabo Roig, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre Cabo Roig, Costa Blanca Sud",
"h1":"Propriété à vendre Cabo Roig"
},
"DE":{
"description":"Cabo Roig Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"Cabo Roig Ferienwohnungen, Cabo Roig Stadth&auml;user, Cabo Roig villas, Costa Blanca S&uuml;d, Spanien",
"title":"Cabo Roig Immobilien zu verkaufen Costa Blanca S&uuml;d",
"h1":"Cabo Roig Immobilien zu verkaufen"
},
"NL":{
"description":"Eigendom te koop in Cabo Roig, Costa Blanca Zuid",
"keywords":"Appartementen Cabo Roig, geschakelde woningen Cabo Roig, villa's Cabo Roig, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop Cabo Roig, Costa Blanca Zuid",
"h1":"Eigendom te koop in Cabo Roig"
},
"pagename_en":"cabo-roig-property-south-costa-blanca-",
"pagename_nl":"Eigendom-te-koop-in-Cabo-Roig-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-a-vendre-a-Cabo-Roig-Costa-Blanca-Sud-",
"pagename_de":"cabo-roig-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"guardamar-del-segura",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strlocation_detail IN('Guardamar','Guardamar del Segura','Guardamar Campo') ORDER BY intprice ASC",
"EN":{
"description":"Guardamar del Segura property for sale in Costa Blanca South",
"keywords":"Guardamar del Segura apartments, Guardamar del Segura townhouses, Guardamar del Segura villas, Costa Blanca South, Spain",
"title":"Guardamar del Segura property for sale South Costa Blanca",
"h1":"Guardamar del Segura Property For Sale"},
"FR":{
"description":"Propriété à vendre à Guardamar del Segura, Costa Blanca Sud",
"keywords":"Appartements Guardamar del Segura, maisons mitoyennes Guardamar del Segura, villas Guardamar del Segura, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre Guardamar del Segura, Costa Blanca Sud",
"h1":"Propriété à vendre Guardamar del Segura"
},
"DE":{
"description":"Guardamar del Segura Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"Guardamar del Segura Ferienwohnungen, Guardamar del Segura Stadth&auml;user, Guardamar del Segura villas, Costa Blanca S&uuml;d, Spanien",
"title":"Guardamar del Segura Immobilien zu verkaufen Costa Blanca S&uuml;d",
"h1":"Guardamar del Segura Immobilien zu verkaufen"
},
"NL":{
"description":"Eigendom te koop in Guardamar del Segura, Costa Blanca Zuid.",
"keywords":"Appartementen Guardamar del Segura, geschakelde woningen Guardamar del Segura, villa's Guardamar del Segura, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop Guardamar del Segura, Costa Blanca Zuid.",
"h1":"Eigendom te koop Guardamar del Segura"
},
"pagename_en":"guardamar-del-segura-property-south-costa-blanca-",
"pagename_nl":"Eigendom-te-koop-in-Guardamar-del-Segura-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-a-vendre-a-Guardamar-del-Segura-Costa-Blanca-Sud-",
"pagename_de":"guardamar-del-segura-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"quesada",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strlocation_detail LIKE('%Quesada%') ORDER BY intprice ASC",
"EN":{
"description":"Quesada property for sale in Costa Blanca South",
"keywords":"Quesada apartments, Quesada townhouses, Quesada villas, Costa Blanca South, Spain",
"title":"Quesada property for sale South Costa Blanca",
"h1":"Quesada Property For Sale"},
"FR":{
"description":"Propriété à vendre à Quesada, Costa Blanca Sud",
"keywords":"Appartements Quesada, maisons mitoyennes Quesada, villas Quesada, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre à Quesada, Costa Blanca Sud",
"h1":"Propriété à vendre à Quesada"
},
"DE":{
"description":"Quesada Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"Quesada Ferienwohnungen, Quesada Stadth&auml;user, Quesada villas, Costa Blanca S&uuml;d, Spanien",
"title":"Quesada Immobilien zu verkaufen Costa Blanca S&uuml;d",
"h1":"Quesada Immobilien zu verkaufen"
},
"NL":{
"description":"Eigendom te koop in Quesada, Costa Blanca Zuid",
"keywords":"Appartementen Quesada, geschakelde woningen Quesada, villa's Quesada, Costa Blanca Zuid, Spanj",
"title":"Eigendom te koop in Quesada, Costa Blanca Zuid",
"h1":"Eigendom te koop in Quesada"
},
"pagename_en":"quesada-property-south-costa-blanca-",
"pagename_nl":"Eigendom-te-koop-in-Quesada-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-a-vendre-a-Quesada-Costa-Blanca-Sud-",
"pagename_de":"quesada-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"la-zenia",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strlocation_detail = 'La Zenia' ORDER BY intprice ASC",
"EN":{
"description":"La Zenia property for sale in Costa Blanca South",
"keywords":"La Zenia apartments, La Zenia townhouses, La Zenia villas, Costa Blanca South, Spain",
"title":"La Zenia property for sale South Costa Blanca",
"h1":"La Zenia Property For Sale"},
"FR":{
"description":"Propriété à vendre à La Zenia, Costa Blanca Sud",
"keywords":"Appartements La Zenia, maisons mitoyennes La Zenia, villas La Zenia, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre La Zenia, Costa Blanca Sud",
"h1":"Propriété à vendre La Zenia"
},
"DE":{
"description":"La Zenia Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"La Zenia Ferienwohnungen, La Zenia Stadth&auml;user, La Zenia villas, Costa Blanca S&uuml;d, Spanien",
"title":"La Zenia Immobilien zu verkaufen Costa Blanca S&uuml;d",
"h1":"La Zenia Immobilien zu verkaufen"
},
"NL":{
"description":"Eigendom te koop in La Zenia, Costa Blanca Zuid",
"keywords":"Appartementen La Zenia, geschakelde woningen La Zenia, villa's La Zenia, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop La Zenia, Costa Blanca Zuid",
"h1":"Eigendom te koop La Zenia"
},
"pagename_en":"la-zenia-property-south-costa-blanca-",
"pagename_nl":"Eigendom-te-koop-in-La-Zenia-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-a-vendre-a-La-ZeniaCosta-Blanca-Sud-",
"pagename_de":"la-zenia-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"los-balcones",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strlocation_detail = 'Los Balcones' ORDER BY intprice ASC",
"EN":{
"description":"Los Balcones property for sale in Costa Blanca South",
"keywords":"Los Balcones apartments, Los Balcones townhouses, Los Balcones villas, Costa Blanca South, Spain",
"title":"Los Balcones property for sale South Costa Blanca",
"h1":"Los Balcones Property For Sale"},
"FR":{
"description":"Propriété à vendre à Los Balcones, Costa Blanca Sud",
"keywords":"Appartements Los Balcones, maisons mitoyennes Los Balcones, villas Los Balcones, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre Los Balcones, Costa Blanca Sud",
"h1":"Propriété à vendre Los Balcones"
},
"DE":{
"description":"Los Balcones Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"Los Balcones Ferienwohnungen, Los Balcones Stadth&auml;user, Los Balcones villas, Costa Blanca S&uuml;d, Spanien",
"title":"Los Balcones Immobilien zu verkaufen Costa Blanca S&uuml;d",
"h1":"Los Balcones Immobilien zu verkaufen"
},
"NL":{
"description":"Eigendom te koop in Los Balcones, Costa Blanca Zuid",
"keywords":"Appartementen Los Balcones, geschakelde woningen Los Balcones, villa's Los Balcones, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop Los Balcones, Costa Blanca Zuid",
"h1":"Eigendom te koop Los Balcones"
},
"pagename_en":"los-balcones-property-south-costa-blanca-",
"pagename_nl":"Eigendom-te-koop-in-Los-Balcones-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-a-vendre-a-Los-Balcones-Costa-Blanca-Sud-",
"pagename_de":"los-balcones-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"punta-prima",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strlocation_detail = 'Punta Prima' ORDER BY intprice ASC",
"EN":{
"description":"Punta Prima property for sale in Costa Blanca South",
"keywords":"Punta Prima apartments, Costa Blanca South, Spain",
"title":"Punta Prima property for sale South Costa Blanca",
"h1":"Punta Prima Property For Sale"},
"FR":{
"description":"Propriété à vendre à Punta Prima, Costa Blanca Sud",
"keywords":"Appartements Punta Prima, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre Punta Prima, Costa Blanca Sud",
"h1":"Propriété à vendre Punta Prima"
},
"DE":{
"description":"Punta Prima Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"Punta Prima Ferienwohnungen, Costa Blanca S&uuml;d, Spanien",
"title":"Punta Prima Immobilien zu verkaufen Costa Blanca S&uuml;d",
"h1":"Punta Prima Immobilien zu verkaufen"
},
"NL":{
"description":"Eigendom te koop in Punta Prima, Costa Blanca Zuid",
"keywords":"Appartementen Punta Prima, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop Punta Prima, Costa Blanca Zuid",
"h1":"Eigendom te koop in Punta Prima"
},
"pagename_en":"punta-prima-property-south-costa-blanca-",
"pagename_nl":"Eigendom-te-koop-in-Punta-Prima-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-a-vendre-a-Punta-Prima-Costa-Blanca-Sud-",
"pagename_de":"punta-prima-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"alameda",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strlocation_detail LIKE ('%Alameda%') ORDER BY intprice ASC",
"EN":{
"description":"Alameda property for sale in Costa Blanca South",
"keywords":"Alameda apartments, Alameda townhouses, Alameda villas, Costa Blanca South, Spain",
"title":"Alameda property for sale South Costa Blanca",
"h1":"Alameda Property For Sale"},
"FR":{
"description":"Propriété à vendre à Alameda, Costa Blanca Sud",
"keywords":"Appartements Alameda, maisons mitoyennes Alameda, villas Alameda, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre Alameda, Costa Blanca Sud",
"h1":"Propriété à vendre Alameda"
},
"DE":{
"description":"Alameda Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"Alameda Ferienwohnungen, Alameda Stadth&auml;user, Alameda villas, Costa Blanca S&uuml;d, Spanien",
"title":"Alameda Immobilien zu verkaufen Costa Blanca S&uuml;d",
"h1":"Alameda Immobilien zu verkaufen"
},
"NL":{
"description":"Eigendom te koop in Alameda, Costa Blanca Zuid",
"keywords":"Appartementen Alameda, geschakelde woningen Alameda, villa's Alameda, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop Alameda, Costa Blanca Zuid",
"h1":"Eigendom te koop Alameda"
},
"pagename_en":"alameda-property-south-costa-blanca-",
"pagename_nl":"Eigendom-te-koop-in-Alameda-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-a-vendre-a-Alameda-Costa-Blanca-Sud-",
"pagename_de":"alameda-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"campoamor",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strlocation_detail LIKE ('%Campoamor%') ORDER BY intprice ASC",
"EN":{
"description":"Campoamor property for sale in Costa Blanca South",
"keywords":"Campoamor apartments, Campoamor townhouses, Campoamor villas, Costa Blanca South, Spain",
"title":"Campoamor property for sale South Costa Blanca",
"h1":"Campoamor Property For Sale"},
"FR":{
"description":"Propriété à vendre à Campoamor, Costa Blanca Sud",
"keywords":"Appartements Campoamor, maisons mitoyennes Campoamor, villas Campoamor, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre Campoamor, Costa Blanca Sud",
"h1":"Propriété à vendre Campoamor"
},
"DE":{
"description":"Campoamor Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"Campoamor Ferienwohnungen, Campoamor Stadth&auml;user, Campoamor villas, Costa Blanca S&uuml;d, Spanien",
"title":"Campoamor Immobilien zu verkaufen Costa Blanca S&uuml;d",
"h1":"Campoamor Immobilien zu verkaufen"
},
"NL":{
"description":"Eigendom te koop in Campoamor, Costa Blanca Zuid",
"keywords":"Appartementen Campoamor, geschakelde woningen Campoamor, villa's Campoamor, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop Campoamor, Costa Blanca Zuid",
"h1":"Eigendom te koop Campoamor"
},
"pagename_en":"campoamor-property-south-costa-blanca-",
"pagename_nl":"Eigendom-te-koop-in-Campoamor-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-a-vendre-a-Campoamor-Costa-Blanca-Sud-",
"pagename_de":"campoamor-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"las-filipinas",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strlocation_detail = 'Las Filipinas' ORDER BY intprice ASC",
"EN":{
"description":"Las Filipinas property for sale in Costa Blanca South",
"keywords":"Las Filipinas apartments, Las Filipinas townhouses, Las Filipinas villas, Costa Blanca South, Spain",
"title":"Las Filipinas property for sale South Costa Blanca",
"h1":"Las Filipinas Property For Sale"},
"FR":{
"description":"Propriété à vendre à Las Filipinas, Costa Blanca Sud",
"keywords":"Appartements Las Filipinas, maisons mitoyennes Las Filipinas, villas Las Filipinas, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre Las Filipinas, Costa Blanca Sud",
"h1":"Propriété à vendre Las Filipinas"
},
"DE":{
"description":"Las Filipinas Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"Las Filipinas Ferienwohnungen, Las Filipinas Stadth&auml;user, Las Filipinas villas, Costa Blanca S&uuml;d, Spanien",
"title":"Las Filipinas Immobilien zu verkaufen Costa Blanca S&uuml;d",
"h1":"Las Filipinas Immobilien zu verkaufen"
},
"NL":{
"description":"Eigendom te koop in Las Filipinas, Costa Blanca Zuid",
"keywords":"Appartementen Las Filipinas, geschakelde woningen Las Filipinas, villa's Las Filipinas, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop Las Filipinas, Costa Blanca Zuid",
"h1":"Eigendom te koop Las Filipinas"
},
"pagename_en":"las-filipinas-property-south-costa-blanca-",
"pagename_nl":"Eigendom-te-koop-in-Las-Filipinas-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-a-vendre-a-Las-Filipinas-Costa-Blanca-Sud-",
"pagename_de":"las-filipinas-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"los-dolses",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strlocation_detail = 'Los Dolses' ORDER BY intprice ASC",
"EN":{
"description":"Los Dolses property for sale in Costa Blanca South",
"keywords":"Los Dolses apartments, Los Dolses townhouses, Los Dolses villas, Costa Blanca South, Spain",
"title":"Los Dolses property for sale South Costa Blanca",
"h1":"Los Dolses Property For Sale"},
"FR":{
"description":"Propriété à vendre à Los Dolses, Costa Blanca Sud",
"keywords":"Appartements Los Dolses, maisons mitoyennes Los Dolses, villas Los Dolses, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre Los Dolses, Costa Blanca Sud",
"h1":"Propriété à vendre Los Dolses"
},
"DE":{
"description":"Los Dolses Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"Los Dolses Ferienwohnungen, Los Dolses Stadth&auml;user, Los Dolses villas, Costa Blanca S&uuml;d, Spanien",
"title":"Los Dolses Immobilien zu verkaufen Costa Blanca S&uuml;d",
"h1":"Los Dolses Immobilien zu verkaufen"
},
"NL":{
"description":"Eigendom te koop in Los Dolses, Costa Blanca Zuid",
"keywords":"Appartementen Los Dolses, geschakelde woningen Los Dolses, villa's Los Dolses, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop Los Dolses, Costa Blanca Zuid",
"h1":"Eigendom te koop Los Dolses"
},
"pagename_en":"los-dolses-property-south-costa-blanca-",
"pagename_nl":"Eigendom-te-koop-in-Los-Dolses-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-a-vendre-a-Los-Dolses-Costa-Blanca-Sud-",
"pagename_de":"los-dolses-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"las-ramblas",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strlocation_detail = 'Las Ramblas' ORDER BY intprice ASC",
"EN":{
"description":"Las Ramblas property for sale in Costa Blanca South",
"keywords":"Las Ramblas apartments, Las Ramblas townhouses, Las Ramblas villas, Costa Blanca South, Spain",
"title":"Las Ramblas property for sale South Costa Blanca",
"h1":"Las Ramblas Property For Sale"},
"FR":{
"description":"Propriété à vendre à Las Ramblas, Costa Blanca Sud",
"keywords":"Appartements Las Ramblas, maisons mitoyennes Las Ramblas, villas Las Ramblas, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre Las Ramblas, Costa Blanca Sud",
"h1":"Propriété à vendre Las Ramblas"
},
"DE":{
"description":"Las Ramblas Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"Las Ramblas Ferienwohnungen, Las Ramblas Stadth&auml;user, Las Ramblas villas, Costa Blanca S&uuml;d, Spanien",
"title":"Las Ramblas Immobilien zu verkaufen Costa Blanca S&uuml;d",
"h1":"Las Ramblas Immobilien zu verkaufen"
},
"NL":{
"description":"Eigendom te koop in Las Ramblas, Costa Blanca Zuid",
"keywords":"Appartementen Las Ramblas, geschakelde woningen Las Ramblas, villa's Las Ramblas, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop Las Ramblas, Costa Blanca Zuid",
"h1":"Eigendom te koop in Las Ramblas"
},
"pagename_en":"las-ramblas-property-south-costa-blanca-",
"pagename_nl":"Eigendom-te-koop-in-Las-Ramblas-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-a-vendre-a-Las-Ramblas-Costa-Blanca-Sud-",
"pagename_de":"las-ramblas-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"rio-mar",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strlocation_detail = 'Rio Mar' ORDER BY intprice ASC",
"EN":{
"description":"Rio Mar property for sale in Costa Blanca South",
"keywords":"Rio Mar apartments, Rio Mar townhouses, Rio Mar villas, Costa Blanca South, Spain",
"title":"Rio Mar property for sale South Costa Blanca",
"h1":"Rio Mar Property For Sale"},
"FR":{
"description":"Propriété à vendre à Rio Mar, Costa Blanca Sud",
"keywords":"Appartements Rio Mar, maisons mitoyennes Rio Mar, villas Rio Mar, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre Rio Mar, Costa Blanca Sud",
"h1":"Propriété à vendre Rio Mar"
},
"DE":{
"description":"Rio Mar Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"Rio Mar Ferienwohnungen, Rio Mar Stadth&auml;user, Rio Mar villas, Costa Blanca S&uuml;d, Spanien",
"title":"Rio Mar Immobilien zu verkaufen Costa Blanca S&uuml;d",
"h1":"Rio Mar Immobilien zu verkaufen"
},
"NL":{
"description":"Eigendom te koop in Rio Mar, Costa Blanca Zuid",
"keywords":"Appartementen Rio Mar, geschakelde woningen Rio Mar, villa's Rio Mar, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop Rio Mar, Costa Blanca Zuid",
"h1":"Eigendom te koop Rio Mar"
},
"pagename_en":"rio-mar-property-south-costa-blanca-",
"pagename_nl":"Eigendom-te-koop-in-Rio-Mar-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-a-vendre-a-Rio-Mar-Costa-Blanca-Sud-",
"pagename_de":"rio-mar-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"torrevieja",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strtown = 'Torrevieja' ORDER BY intprice ASC",
"EN":{
"description":"Torrevieja property for sale in Costa Blanca South",
"keywords":"Torrevieja apartments, Torrevieja townhouses, Torrevieja villas, Costa Blanca South, Spain",
"title":"Torrevieja property for sale South Costa Blanca",
"h1":"Torrevieja Property For Sale"},
"FR":{
"description":"Propriété à vendre à Torrevieja, Costa Blanca Sud",
"keywords":"Appartements Torrevieja, maisons mitoyennes Torrevieja, villas Torrevieja, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre Torrevieja, Costa Blanca Sud",
"h1":"Propriété à vendre Torrevieja"
},
"DE":{
"description":"Torrevieja Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"Torrevieja Ferienwohnungen, Torrevieja Stadth&auml;user, Torrevieja villas, Costa Blanca S&uuml;d, Spanien",
"title":"Torrevieja Immobilien zu verkaufen Costa Blanca S&uuml;d",
"h1":"Torrevieja Immobilien zu verkaufen"
},
"NL":{
"description":"Eigendom te koop in Torrevieja, Costa Blanca Zuid",
"keywords":"Appartementen Torrevieja, geschakelde woningen Torrevieja, villa's Torrevieja, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop Torrevieja, Costa Blanca Zuid",
"h1":"Eigendom te koop Torrevieja"
},
"pagename_en":"torrevieja-property-south-costa-blanca-",
"pagename_nl":"Eigendom-te-koop-in-Torrevieja-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-a-vendre-a-Torrevieja-Costa-Blanca-Sud-",
"pagename_de":"torrevieja-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"dream-hills",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strlocation_detail = 'Dream Hills' ORDER BY intprice ASC",
"EN":{
"description":"Dream Hills property for sale in Costa Blanca South",
"keywords":"Dream Hills apartments, Dream Hills townhouses, Dream Hills villas, Costa Blanca South, Spain",
"title":"Dream Hills property for sale South Costa Blanca",
"h1":"Dream Hills Property For Sale"},
"FR":{
"description":"Propriété à vendre à Dream Hills, Costa Blanca Sud",
"keywords":"Appartements Dream Hills, maisons mitoyennes Dream Hills, villas Dream Hills, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre Dream Hills, Costa Blanca Sud",
"h1":"Propriété à vendre Dream Hills"
},
"DE":{
"description":"Dream Hills Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"Dream Hills Ferienwohnungen, Dream Hills Stadth&auml;user, Dream Hills villas, Costa Blanca S&uuml;d, Spanien",
"title":"Dream Hills Immobilien zu verkaufen Costa Blanca S&uuml;d",
"h1":"Dream Hills Immobilien zu verkaufen"
},
"NL":{
"description":"Eigendom te koop in Dream Hills, Costa Blanca Zuid",
"keywords":"Appartementen Dream Hills, geschakelde woningen Dream Hills, villa's Dream Hills, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop Dream Hills, Costa Blanca Zuid",
"h1":"Eigendom te koop Dream Hills"
},
"pagename_en":"dream-hills-property-south-costa-blanca-",
"pagename_nl":"Eigendom-te-koop-in-Dream-Hills-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-a-vendre-a-Dream-Hills-Costa-Blanca-Sud-",
"pagename_de":"dream-hills-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"algorfa",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strlocation_detail = 'Algorfa' ORDER BY intprice ASC",
"EN":{
"description":"Algorfa property for sale in Costa Blanca South",
"keywords":"Algorfa apartments, Algorfa townhouses, Algorfa villas, Costa Blanca South, Spain",
"title":"Algorfa property for sale South Costa Blanca",
"h1":"Algorfa Property For Sale"},
"FR":{
"description":"Propriété à vendre à Algorfa, Costa Blanca Sud",
"keywords":"Appartements Algorfa, maisons mitoyennes Algorfa, villas Algorfa, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre Algorfa, Costa Blanca Sud",
"h1":"Propriété à vendre Algorfa"
},
"DE":{
"description":"Algorfa Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"Algorfa Ferienwohnungen, Algorfa Stadth&auml;user, Algorfa villas, Costa Blanca S&uuml;d, Spanien",
"title":"Algorfa Immobilien zu verkaufen Costa Blanca S&uuml;d",
"h1":"Algorfa Immobilien zu verkaufen"
},
"NL":{
"description":"Eigendom te koop in Algorfa, Costa Blanca Zuid",
"keywords":"Appartementen Algorfa, geschakelde woningen Algorfa, villa's Algorfa, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop Algorfa, Costa Blanca Zuid",
"h1":"Eigendom te koop Algorfa"
},
"pagename_en":"algorfa-property-south-costa-blanca-",
"pagename_nl":"Eigendom-te-koop-in-Algorfa-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-a-vendre-a-Algorfa-Costa-Blanca-Sud-",
"pagename_de":"algorfa-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"la-mata",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strlocation_detail = 'La Mata' ORDER BY intprice ASC",
"EN":{
"description":"La Mata property for sale in Costa Blanca South",
"keywords":"La Mata apartments, La Mata townhouses, La Mata villas, Costa Blanca South, Spain",
"title":"La Mata property for sale South Costa Blanca",
"h1":"La Mata Property For Sale"},
"FR":{
"description":"Propriété à vendre à La Mata, Costa Blanca Sud",
"keywords":"Appartements La Mata, maisons mitoyennes La Mata, villas La Mata, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre La Mata, Costa Blanca Sud",
"h1":"Propriété à vendre La Mata"
},
"DE":{
"description":"La Mata Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"La Mata Ferienwohnungen, La Mata Stadth&auml;user, La Mata villas, Costa Blanca S&uuml;d, Spanien",
"title":"La Mata Immobilien zu verkaufen Costa Blanca S&uuml;d",
"h1":"La Mata Immobilien zu verkaufen"
},
"NL":{
"description":"Eigendom te koop in La Mata, Costa Blanca Zuid",
"keywords":"Appartementen La Mata, geschakelde woningen La Mata, villa's La Mata, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop La Mata, Costa Blanca Zuid",
"h1":"Eigendom te koop La Mata"
},
"pagename_en":"la-mata-property-south-costa-blanca-",
"pagename_nl":"Eigendom-te-koop-in-La-Mata-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-a-vendre-a-La-Mata-Costa-Blanca-Sud-",
"pagename_de":"la-mata-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"la torreta",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strlocation_detail = 'La Torreta' ORDER BY intprice ASC",
"EN":{
"description":"La Torreta property for sale in Costa Blanca South",
"keywords":"La Torreta apartments, La Torreta townhouses, La Torreta villas, Costa Blanca South, Spain",
"title":"La Torreta property for sale South Costa Blanca",
"h1":"La Torreta Property For Sale"},
"FR":{
"description":"Propriété à vendre à La Torreta, Costa Blanca Sud",
"keywords":"Appartements La Torreta, maisons mitoyennes La Torreta, villas La Torreta, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre La Torreta, Costa Blanca Sud",
"h1":"Propriété à vendre La Torreta"
},
"DE":{
"description":"La Torreta Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"La Torreta Ferienwohnungen, La Torreta Stadth&auml;user, La Torreta villas, Costa Blanca S&uuml;d, Spanien",
"title":"La Torreta Immobilien zu verkaufen Costa Blanca S&uuml;d",
"h1":"La Torreta Immobilien zu verkaufen"
},
"NL":{
"description":"Eigendom te koop in La Torreta, Costa Blanca Zuid",
"keywords":"Appartementen La Torreta, geschakelde woningen La Torreta, villa's La Torreta, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop La Torreta, Costa Blanca Zuid",
"h1":"Eigendom te koop La Torreta"
},
"pagename_en":"la-torreta-property-south-costa-blanca-",
"pagename_nl":"Eigendom-te-koop-in-La-Torreta-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-a-vendre-a-La-Torreta-Costa-Blanca-Sud-",
"pagename_de":"la-torreta-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"los-altos",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strlocation_detail = 'Los Altos' ORDER BY intprice ASC",
"EN":{
"description":"Los Altos property for sale in Costa Blanca South",
"keywords":"Los Altos apartments, Los Altos townhouses, Los Altos villas, Costa Blanca South, Spain",
"title":"Los Altos property for sale South Costa Blanca",
"h1":"Los Altos Property For Sale"},
"FR":{
"description":"Propriété à vendre à Los Altos, Costa Blanca Sud",
"keywords":"Appartements Los Altos, maisons mitoyennes Los Altos, villas Los Altos, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre Los Altos, Costa Blanca Sud",
"h1":"Propriété à vendre Los Altos"
},
"DE":{
"description":"Los Altos Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"Los Altos Ferienwohnungen, Los Altos Stadth&auml;user, Los Altos villas, Costa Blanca S&uuml;d, Spanien",
"title":"Los Altos Immobilien zu verkaufen Costa Blanca S&uuml;d",
"h1":"Los Altos Immobilien zu verkaufen"
},
"NL":{
"description":"Eigendom te koop in Los Altos, Costa Blanca Zuid",
"keywords":"Appartementen Los Altos, geschakelde woningen Los Altos, villa's Los Altos, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop Los Altos, Costa Blanca Zuid",
"h1":"Eigendom te koop Los Altos"
},
"pagename_en":"los-altos-property-south-costa-blanca-",
"pagename_nl":"Eigendom-te-koop-in-Los-Altos-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-a-vendre-a-Los-Altos-Costa-Blanca-Sud-",
"pagename_de":"los-altos-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"mar-azul",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strlocation_detail = 'Mar Azul' ORDER BY intprice ASC",
"EN":{"description":"Mar Azul property for sale in Costa Blanca South",
"keywords":"Mar Azul apartments, Mar Azul townhouses, Mar Azul villas, Costa Blanca South, Spain",
"title":"Mar Azul property for sale South Costa Blanca",
"h1":"Mar Azul Property For Sale"},
"FR":{
"description":"Propriété à vendre à Mar Azul, Costa Blanca Sud",
"keywords":"Appartements Mar Azul, maisons mitoyennes Mar Azul, villas Mar Azul, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre Mar Azul, Costa Blanca Sud",
"h1":"Propriété à vendre Mar Azul"
},
"DE":{
"description":"Mar Azul Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"Mar Azul Ferienwohnungen, Mar Azul Stadth&auml;user, Mar Azul villas, Costa Blanca S&uuml;d, Spanien",
"title":"Mar Azul Immobilien zu verkaufen Costa Blanca S&uuml;d",
"h1":"Mar Azul Immobilien zu verkaufen"
},
"NL":{
"description":"Eigendom te koop in Mar Azul, Costa Blanca Zuid",
"keywords":"Appartementen Mar Azul, geschakelde woningen Mar Azul, villa's Mar Azul, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop Mar Azul, Costa Blanca Zuid",
"h1":"Eigendom te koop Mar Azul"
},
"pagename_en":"mar-azul-property-south-costa-blanca-",
"pagename_nl":"Eigendom-te-koop-in-Mar-Azul-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-a-vendre-a-Mar-Azul-Costa-Blanca-Sud-",
"pagename_de":"mar-azul-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"miraflores",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strlocation_detail = 'Miraflores' ORDER BY intprice ASC",
"EN":{
"description":"Miraflores property for sale in Costa Blanca South",
"keywords":"Miraflores apartments, Miraflores townhouses, Miraflores villas, Costa Blanca South, Spain",
"title":"Miraflores property for sale South Costa Blanca",
"h1":"Miraflores Property For Sale"},
"FR":{
"description":"Propriété à vendre à Miraflores, Costa Blanca Sud",
"keywords":"Appartements Miraflores, maisons mitoyennes Miraflores, villas Miraflores, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre Miraflores, Costa Blanca Sud",
"h1":"Propriété à vendre Miraflores"
},
"DE":{
"description":"Miraflores Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"Miraflores Ferienwohnungen, Miraflores Stadth&auml;user, Miraflores villas, Costa Blanca S&uuml;d, Spanien",
"title":"Miraflores Immobilien zu verkaufen Costa Blanca S&uuml;d",
"h1":"Miraflores Immobilien zu verkaufen"
},
"NL":{
"description":"Eigendom te koop in Miraflores, Costa Blanca Zuid",
"keywords":"Appartementen Miraflores, geschakelde woningen Miraflores, villa's Miraflores, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop Miraflores, Costa Blanca Zuid",
"h1":"Eigendom te koop Miraflores"
},
"pagename_en":"miraflores-property-south-costa-blanca-",
"pagename_nl":"Eigendom-te-koop-in-Miraflores-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-a-vendre-a-Miraflores-Costa-Blanca-Sud-",
"pagename_de":"miraflores-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"rocio-del-mar",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strlocation_detail = 'Rocio del Mar' ORDER BY intprice ASC",
"EN":{
"description":"Rocio del Mar property for sale in Costa Blanca South",
"keywords":"Rocio del Mar apartments, Rocio del Mar townhouses, Rocio del Mar villas, Costa Blanca South, Spain",
"title":"Rocio del Mar property for sale South Costa Blanca",
"h1":"Rocio del Mar Property For Sale"},
"FR":{
"description":"Propriété à vendre à Rocio del Mar, Costa Blanca Sud",
"keywords":"Appartements Rocio del Mar, maisons mitoyennes Rocio del Mar, villas Rocio del Mar, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre Rocio del Mar, Costa Blanca Sud",
"h1":"Propriété à vendre Rocio del Mar"
},
"DE":{
"description":"Rocio del Mar Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"Rocio del Mar Ferienwohnungen, Rocio del Mar Stadth&auml;user, Rocio del Mar villas, Costa Blanca S&uuml;d, Spanien",
"title":"Rocio del Mar Immobilien zu verkaufen Costa Blanca S&uuml;d",
"h1":"Rocio del Mar Immobilien zu verkaufen"
},
"NL":{
"description":"Eigendom te koop in Rocio del Mar, Costa Blanca Zuid",
"keywords":"Appartementen Rocio del Mar, geschakelde woningen Rocio del Mar, villa's Rocio del Mar, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop Rocio del Mar, Costa Blanca Zuid",
"h1":"Eigendom te koop Rocio del Mar"
},
"pagename_en":"rocio-del-mar-property-south-costa-blanca-",
"pagename_nl":"Eigendom-te-koop-in-Rocio-del-Mar-Costa-Blanca-Zuid-",
"pagename_fr":"Propriete-a-vendre-a-Rocio-del-Mar-Costa-Blanca-Sud-",
"pagename_de":"rocio-del-mar-Immobilien-costa-blanca-sud-"
},
{
"rubrun":"la-manga",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strlocation_detail Like 'La Manga%' ORDER BY intprice ASC",
"EN":{
"description":"La Manga property for sale in Costa Blanca South",
"keywords":"La Manga apartments, La Manga townhouses, La Manga villas, Costa Blanca South, Spain",
"title":"La Manga property for sale Murcia",
"h1":"La Manga del Mar Menor Property For Sale"},
"FR":{
"description":"Propriété à vendre à La Manga, Costa Blanca Sud",
"keywords":"Appartements La Manga, maisons mitoyennes La Manga, villas La Manga, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre La Manga, Murcia",
"h1":"Propriété à vendre La Manga del Mar Menor"
},
"DE":{
"description":"La Manga Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"La Manga Ferienwohnungen, La Manga Stadth&auml;user, La Manga villas, Costa Blanca S&uuml;d, Spanien",
"title":"La Manga Immobilien zu verkaufen Murcia",
"h1":"La Manga del Mar Menor Immobilien zu verkaufen"
},
"NL":{
"description":"Eigendom te koop in La Manga, Costa Blanca Zuid",
"keywords":"Appartementen La Manga, geschakelde woningen La Manga, villa's La Manga, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop La Manga, Murcia",
"h1":"Eigendom te koop in La Manga del Mar Menor"
},
"pagename_en":"la-manga-property-murcia-",
"pagename_nl":"Eigendom-te-koop-in-La-Manga-del-Mar-Menor-",
"pagename_fr":"Propriete-a-vendre-a-La-Manga-del-Mar-Menor-",
"pagename_de":"la-manga-Immobilien-murcia-"
},
{
"rubrun":"los-alcazares",
"query":"SELECT * FROM  mghprops WHERE  blndisplay = 1 AND blnrental = 0 AND strtown = 'Los Alcazares' ORDER BY intprice ASC",
"EN":{
"description":"Los Alcazares property for sale in Costa Blanca South",
"keywords":"Los Alcazares apartments, Los Alcazares townhouses, Los Alcazares villas, Costa Blanca South, Spain",
"title":"Los Alcazares property for sale Murcia",
"h1":"Los Alcazares Property For Sale"},
"FR":{
"description":"Propriété à vendre à Los Alcazares, Costa Blanca Sud",
"keywords":"Appartements Los Alcazares, maisons mitoyennes Los Alcazares, villas Los Alcazares, Costa Blanca Sud, Espagne",
"title":"Propriété à vendre Los Alcazares, Murcia",
"h1":"Propriété à vendre Los Alcazares"
},
"DE":{
"description":"Los Alcazares Immobilien zu verkaufen in Costa Blanca S&uuml;d",
"keywords":"Los Alcazares Ferienwohnungen, Los Alcazares Stadth&auml;user, Los Alcazares villas, Costa Blanca S&uuml;d, Spanien",
"title":"Los Alcazares Immobilien zu verkaufen Murcia",
"h1":"Los Alcazares Immobilien zu verkaufen"
},
"NL":{
"description":"Eigendom te koop in Los Alcazares, Costa Blanca Zuid",
"keywords":"Appartementen Los Alcazares, geschakelde woningen Los Alcazares, villa's Los Alcazares, Costa Blanca Zuid, Spanje",
"title":"Eigendom te koop Los Alcazares, Murcia",
"h1":"Eigendom te koop Los Alcazares"
},
"pagename_en":"los-alcazares-property-murcia-",
"pagename_nl":"Eigendom-te-koop-in-Los-Alcazares-murcia-",
"pagename_fr":"Propriete-a-vendre-a-Los-Alcazares-Murcia-",
"pagename_de":"los-alcazares-Immobilien-murcia-"
}
]
