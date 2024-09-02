LINK_TEMPLATES = {
    'sectors':"https://search.worldbank.org/api/v3/projects?format=json&fct=projectfinancialtype_exact,status_exact,countryshortname_exact,sector_exact,theme_exact,regionname_exact,fiscalyear&fl=id,status,project_name,countryshortname,boardapprovaldate,totalcommamt_srt,countrycode,regionname&statsfield=totalamt,totalcommamt_srt&statsfacet=countryshortname_exact^regionname_exact^fiscalyear&rows=6&os=0&srt=boardapprovaldate&order=desc&apilang=en&status_exact=Active^Closed&prodline_exact=GU^PE&countrycode_exact={sort_name}&os=0",
    
    'sectors_information': "https://data.worldbank.org/model.json?paths=%5B%5B%22countryMeta%22%2C%22{sort_name}%22%2C%5B%22adminregion%22%2C%22en%22%2C%22id%22%2C%22incomelevel%22%2C%22locationType%22%2C%22locations%22%2C%22name%22%2C%22region%22%5D%5D%2C%5B%22indicatorMeta%22%2C%5B%22AG.LND.AGRI.ZS%22%2C%22AG.LND.EL5M.UR.K2%22%2C%22AG.LND.EL5M.ZS%22%2C%22AG.LND.FRST.ZS%22%2C%22AG.PRD.CROP.XD%22%2C%22AG.PRD.LVSK.XD%22%2C%22BN.GSR.GNFS.CD%22%2C%22BN.KLT.DINV.CD%22%2C%22BX.KLT.DINV.WD.GD.ZS%22%2C%22BX.TRF.PWKR.DT.GD.ZS%22%2C%22CM.MKT.TRAD.GD.ZS%22%2C%22DT.TDS.DPPF.XP.ZS%22%2C%22EG.CFT.ACCS.ZS%22%2C%22EG.ELC.ACCS.RU.ZS%22%2C%22EG.ELC.ACCS.UR.ZS%22%2C%22EG.ELC.ACCS.ZS%22%2C%22EG.ELC.RNWX.ZS%22%2C%22EG.FEC.RNEW.ZS%22%2C%22EG.USE.COMM.CL.ZS%22%2C%22EG.USE.ELEC.KH.PC%22%2C%22EN.ATM.CO2E.PC%22%2C%22EN.ATM.GHGT.KT.CE%22%2C%22EN.ATM.PM25.MC.ZS%22%2C%22EN.CLC.DRSK.XQ%22%2C%22EN.CLC.MDAT.ZS%22%2C%22EN.CO2.TRAN.ZS%22%2C%22EN.POP.SLUM.UR.ZS%22%2C%22ER.FSH.AQUA.MT%22%2C%22ER.FSH.CAPT.MT%22%2C%22ER.FSH.PROD.MT%22%2C%22ER.H2O.FWST.ZS%22%2C%22ER.H2O.FWTL.ZS%22%2C%22ER.LND.PTLD.ZS%22%2C%22ER.MRN.PTMR.ZS%22%2C%22ER.PTD.TOTL.ZS%22%2C%22FP.CPI.TOTL.ZG%22%2C%22FX.OWN.TOTL.ZS%22%2C%22GB.XPD.RSDV.GD.ZS%22%2C%22GC.DOD.TOTL.GD.ZS%22%2C%22GC.REV.SOCL.ZS%22%2C%22GC.TAX.TOTL.GD.ZS%22%2C%22GF.XPD.BUDG.ZS%22%2C%22HD.HCI.OVRL%22%2C%22IC.FRM.BNKS.ZS%22%2C%22IC.FRM.BRIB.ZS%22%2C%22IC.FRM.FEMM.ZS%22%2C%22IE.PPN.ENGY.CD%22%2C%22IE.PPN.TRAN.CD%22%2C%22IE.PPN.WATR.CD%22%2C%22IQ.SPI.OVRL%22%2C%22IS.RRS.GOOD.MT.K6%22%2C%22IS.RRS.PASG.KM%22%2C%22IT.CEL.SETS.P2%22%2C%22IT.NET.BBND.P2%22%2C%22IT.NET.USER.ZS%22%2C%22LP.LPI.ITRN.XQ%22%2C%22MS.MIL.TOTL.TF.ZS%22%2C%22MS.MIL.XPND.GD.ZS%22%2C%22NE.EXP.GNFS.ZS%22%2C%22NV.AGR.TOTL.ZS%22%2C%22NV.IND.MANF.ZS%22%2C%22NY.ADJ.DFOR.GN.ZS%22%2C%22NY.ADJ.SVNX.GN.ZS%22%2C%22NY.GDP.MKTP.CD%22%2C%22NY.GDP.MKTP.CN%22%2C%22NY.GDP.MKTP.KD%22%2C%22NY.GDP.MKTP.KD.ZG%22%2C%22NY.GDP.MKTP.KN%22%2C%22NY.GDP.PCAP.CD%22%2C%22NY.GDP.PCAP.CN%22%2C%22NY.GDP.PCAP.KD%22%2C%22NY.GDP.PCAP.KD.ZG%22%2C%22NY.GDP.PCAP.KN%22%2C%22NY.GDP.TOTL.RT.ZS%22%2C%22NY.GNP.MKTP.CD%22%2C%22NY.GNP.MKTP.CN%22%2C%22NY.GNP.MKTP.KD%22%2C%22NY.GNP.MKTP.KN%22%2C%22NY.GNP.PCAP.KD.ZG%22%2C%22SE.ADT.1524.LT.ZS%22%2C%22SE.ADT.LITR.ZS%22%2C%22SE.ENR.PRSC.FM.ZS%22%2C%22SE.PRM.CMPT.ZS%22%2C%22SE.PRM.ENRR%22%2C%22SE.SEC.CMPT.LO.FE.ZS%22%2C%22SE.SEC.CMPT.LO.MA.ZS%22%2C%22SE.SEC.CMPT.LO.ZS%22%2C%22SE.XPD.TOTL.GB.ZS%22%2C%22SG.GEN.PARL.ZS%22%2C%22SG.LAW.INDX%22%2C%22SH.DYN.AIDS.ZS%22%2C%22SH.DYN.MORT%22%2C%22SH.DYN.MORT.FE%22%2C%22SH.DYN.MORT.MA%22%2C%22SH.H2O.BASW.ZS%22%2C%22SH.H2O.SMDW.ZS%22%2C%22SH.HIV.INCD.ZS%22%2C%22SH.IMM.MEAS%22%2C%22SH.SGR.CRSK.ZS%22%2C%22SH.STA.BASS.ZS%22%2C%22SH.STA.HYGN.ZS%22%2C%22SH.STA.MMRT%22%2C%22SH.STA.SMSS.ZS%22%2C%22SH.STA.STNT.FE.ZS%22%2C%22SH.STA.STNT.MA.ZS%22%2C%22SH.STA.STNT.ZS%22%2C%22SH.STA.TRAF.P5%22%2C%22SI.DST.50MD%22%2C%22SI.DST.FRST.20%22%2C%22SI.POV.DDAY%22%2C%22SI.POV.GINI%22%2C%22SI.POV.MDIM%22%2C%22SI.POV.NAHC%22%2C%22SI.RMT.COST.IB.ZS%22%2C%22SI.RMT.COST.OB.ZS%22%2C%22SI.SPR.PC40.ZG%22%2C%22SI.SPR.PCAP.ZG%22%2C%22SL.EMP.SMGT.FE.ZS%22%2C%22SL.EMP.TOTL.SP.ZS%22%2C%22SL.FAM.0714.ZS%22%2C%22SL.GDP.PCAP.EM.KD%22%2C%22SL.TLF.0714.ZS%22%2C%22SL.TLF.CACT.ZS%22%2C%22SL.UEM.TOTL.ZS%22%2C%22SM.POP.NETM%22%2C%22SM.POP.REFG%22%2C%22SN.ITK.DEFC.ZS%22%2C%22SN.ITK.SVFI.ZS%22%2C%22SP.ADO.TFRT%22%2C%22SP.DYN.CONU.ZS%22%2C%22SP.DYN.LE00.IN%22%2C%22SP.POP.GROW%22%2C%22SP.POP.TOTL%22%2C%22SP.REG.BRTH.RU.ZS%22%2C%22SP.REG.BRTH.UR.ZS%22%2C%22SP.REG.BRTH.ZS%22%2C%22SP.URB.GROW%22%2C%22SP.URB.TOTL.IN.ZS%22%2C%22TX.VAL.TECH.MF.ZS%22%2C%22VC.IDP.NWDS%22%2C%22VC.IHR.PSRC.P5%22%2C%22per_allsp.cov_pop_tot%22%5D%2C%5B%22License_Type%22%2C%22License_URL%22%2C%22WDITable%22%2C%22decimal%22%2C%22description%22%2C%22en%22%2C%22fullname%22%2C%22id%22%2C%22last_year%22%2C%22relatedIndicators%22%2C%22shortname%22%2C%22source%22%2C%22sourceNote%22%2C%22sourceOrganization%22%2C%22sourceURL%22%2C%22topics%22%2C%22unit%22%5D%5D%5D&method=get",
    'projects_and_operations': "https://data.worldbank.org/model.json?paths=%5B%5B%22extraData%22%2C%5B%22climate%22%2C%22finances%22%2C%22human_capital_index%22%2C%22projects%22%2C%22prospects%22%2C%22subnational%22%2C%22surveys%22%2C%22templateUrls%22%5D%2C%22{sort_name}%22%5D%5D&method=get",


    'indicator':"https://data.worldbank.org/model.json?paths=%5B%5B%22indicatorData%22%2C%22{sort_name}%22%2C%5B%22AG.LND.AGRI.ZS%22%2C%22AG.LND.EL5M.UR.K2%22%2C%22AG.LND.EL5M.ZS%22%2C%22AG.LND.FRST.ZS%22%2C%22AG.PRD.CROP.XD%22%2C%22AG.PRD.LVSK.XD%22%2C%22BN.GSR.GNFS.CD%22%2C%22BN.KLT.DINV.CD%22%2C%22BX.KLT.DINV.WD.GD.ZS%22%2C%22BX.TRF.PWKR.DT.GD.ZS%22%2C%22CM.MKT.TRAD.GD.ZS%22%2C%22DT.TDS.DPPF.XP.ZS%22%2C%22EG.CFT.ACCS.ZS%22%2C%22EG.ELC.ACCS.RU.ZS%22%2C%22EG.ELC.ACCS.UR.ZS%22%2C%22EG.ELC.ACCS.ZS%22%2C%22EG.ELC.RNWX.ZS%22%2C%22EG.FEC.RNEW.ZS%22%2C%22EG.USE.COMM.CL.ZS%22%2C%22EG.USE.ELEC.KH.PC%22%2C%22EN.ATM.CO2E.PC%22%2C%22EN.ATM.GHGT.KT.CE%22%2C%22EN.ATM.PM25.MC.ZS%22%2C%22EN.CLC.DRSK.XQ%22%2C%22EN.CLC.MDAT.ZS%22%2C%22EN.CO2.TRAN.ZS%22%2C%22EN.POP.SLUM.UR.ZS%22%2C%22ER.FSH.AQUA.MT%22%2C%22ER.FSH.CAPT.MT%22%2C%22ER.FSH.PROD.MT%22%2C%22ER.H2O.FWST.ZS%22%2C%22ER.H2O.FWTL.ZS%22%2C%22ER.LND.PTLD.ZS%22%2C%22ER.MRN.PTMR.ZS%22%2C%22ER.PTD.TOTL.ZS%22%2C%22FP.CPI.TOTL.ZG%22%2C%22FX.OWN.TOTL.ZS%22%2C%22GB.XPD.RSDV.GD.ZS%22%2C%22GC.DOD.TOTL.GD.ZS%22%2C%22GC.REV.SOCL.ZS%22%2C%22GC.TAX.TOTL.GD.ZS%22%2C%22GF.XPD.BUDG.ZS%22%2C%22HD.HCI.OVRL%22%2C%22IC.FRM.BNKS.ZS%22%2C%22IC.FRM.BRIB.ZS%22%2C%22IC.FRM.FEMM.ZS%22%2C%22IE.PPN.ENGY.CD%22%2C%22IE.PPN.TRAN.CD%22%2C%22IE.PPN.WATR.CD%22%2C%22IQ.SPI.OVRL%22%2C%22IS.RRS.GOOD.MT.K6%22%2C%22IS.RRS.PASG.KM%22%2C%22IT.CEL.SETS.P2%22%2C%22IT.NET.BBND.P2%22%2C%22IT.NET.USER.ZS%22%2C%22LP.LPI.ITRN.XQ%22%2C%22MS.MIL.TOTL.TF.ZS%22%2C%22MS.MIL.XPND.GD.ZS%22%2C%22NE.EXP.GNFS.ZS%22%2C%22NV.AGR.TOTL.ZS%22%2C%22NV.IND.MANF.ZS%22%2C%22NY.ADJ.DFOR.GN.ZS%22%2C%22NY.ADJ.SVNX.GN.ZS%22%2C%22NY.GDP.MKTP.CD%22%2C%22NY.GDP.MKTP.CN%22%2C%22NY.GDP.MKTP.KD%22%2C%22NY.GDP.MKTP.KD.ZG%22%2C%22NY.GDP.MKTP.KN%22%2C%22NY.GDP.PCAP.CD%22%2C%22NY.GDP.PCAP.CN%22%2C%22NY.GDP.PCAP.KD%22%2C%22NY.GDP.PCAP.KD.ZG%22%2C%22NY.GDP.PCAP.KN%22%2C%22NY.GDP.TOTL.RT.ZS%22%2C%22NY.GNP.MKTP.CD%22%2C%22NY.GNP.MKTP.CN%22%2C%22NY.GNP.MKTP.KD%22%2C%22NY.GNP.MKTP.KN%22%2C%22NY.GNP.PCAP.KD.ZG%22%2C%22SE.ADT.1524.LT.ZS%22%2C%22SE.ADT.LITR.ZS%22%2C%22SE.ENR.PRSC.FM.ZS%22%2C%22SE.PRM.CMPT.ZS%22%2C%22SE.PRM.ENRR%22%2C%22SE.SEC.CMPT.LO.FE.ZS%22%2C%22SE.SEC.CMPT.LO.MA.ZS%22%2C%22SE.SEC.CMPT.LO.ZS%22%2C%22SE.XPD.TOTL.GB.ZS%22%2C%22SG.GEN.PARL.ZS%22%2C%22SG.LAW.INDX%22%2C%22SH.DYN.AIDS.ZS%22%2C%22SH.DYN.MORT%22%2C%22SH.DYN.MORT.FE%22%2C%22SH.DYN.MORT.MA%22%2C%22SH.H2O.BASW.ZS%22%2C%22SH.H2O.SMDW.ZS%22%2C%22SH.HIV.INCD.ZS%22%2C%22SH.IMM.MEAS%22%2C%22SH.SGR.CRSK.ZS%22%2C%22SH.STA.BASS.ZS%22%2C%22SH.STA.HYGN.ZS%22%2C%22SH.STA.MMRT%22%2C%22SH.STA.SMSS.ZS%22%2C%22SH.STA.STNT.FE.ZS%22%2C%22SH.STA.STNT.MA.ZS%22%2C%22SH.STA.STNT.ZS%22%2C%22SH.STA.TRAF.P5%22%2C%22SI.DST.50MD%22%2C%22SI.DST.FRST.20%22%2C%22SI.POV.DDAY%22%2C%22SI.POV.GINI%22%2C%22SI.POV.MDIM%22%2C%22SI.POV.NAHC%22%2C%22SI.RMT.COST.IB.ZS%22%2C%22SI.RMT.COST.OB.ZS%22%2C%22SI.SPR.PC40.ZG%22%2C%22SI.SPR.PCAP.ZG%22%2C%22SL.EMP.SMGT.FE.ZS%22%2C%22SL.EMP.TOTL.SP.ZS%22%2C%22SL.FAM.0714.ZS%22%2C%22SL.GDP.PCAP.EM.KD%22%2C%22SL.TLF.0714.ZS%22%2C%22SL.TLF.CACT.ZS%22%2C%22SL.UEM.TOTL.ZS%22%2C%22SM.POP.NETM%22%2C%22SM.POP.REFG%22%2C%22SN.ITK.DEFC.ZS%22%2C%22SN.ITK.SVFI.ZS%22%2C%22SP.ADO.TFRT%22%2C%22SP.DYN.CONU.ZS%22%2C%22SP.DYN.LE00.IN%22%2C%22SP.POP.GROW%22%2C%22SP.POP.TOTL%22%2C%22SP.REG.BRTH.RU.ZS%22%2C%22SP.REG.BRTH.UR.ZS%22%2C%22SP.REG.BRTH.ZS%22%2C%22SP.URB.GROW%22%2C%22SP.URB.TOTL.IN.ZS%22%2C%22TX.VAL.TECH.MF.ZS%22%2C%22VC.IDP.NWDS%22%2C%22VC.IHR.PSRC.P5%22%2C%22per_allsp.cov_pop_tot%22%5D%2C%7B%22from%22%3A2000%2C%22to%22%3A2023%7D%5D%5D&method=get",
    'indicator_meta_data': "https://data.worldbank.org/model.json?paths=%5B%5B%22indicatorMeta%22%2C%5B%22SL.TLF.TOTL.IN%22%2C%22SM.POP.TOTL%22%2C%22SM.POP.TOTL.ZS%22%2C%22SP.POP.2529.FE.5Y%22%2C%22SP.POP.TOTL.FE.IN%22%2C%22SP.POP.TOTL.FE.ZS%22%2C%22SP.POP.TOTL.MA.IN%22%2C%22SP.POP.TOTL.MA.ZS%22%5D%2C%5B%22License_Type%22%2C%22License_URL%22%2C%22WDITable%22%2C%22decimal%22%2C%22description%22%2C%22en%22%2C%22fullname%22%2C%22id%22%2C%22last_year%22%2C%22relatedIndicators%22%2C%22shortname%22%2C%22source%22%2C%22sourceNote%22%2C%22sourceOrganization%22%2C%22sourceURL%22%2C%22topics%22%2C%22unit%22%5D%5D%5D&method=get",
    'country_information': "https://data.worldbank.org/model.json?paths=%5B%5B%22countryMeta%22%2C%22{sort_name}%22%2C%5B%22adminregion%22%2C%22en%22%2C%22id%22%2C%22incomelevel%22%2C%22locationType%22%2C%22locations%22%2C%22name%22%2C%22region%22%5D%5D%2C%5B%22indicatorMeta%22%2C%5B%22AG.LND.AGRI.ZS%22%2C%22AG.LND.EL5M.UR.K2%22%2C%22AG.LND.EL5M.ZS%22%2C%22AG.LND.FRST.ZS%22%2C%22AG.PRD.CROP.XD%22%2C%22AG.PRD.LVSK.XD%22%2C%22BN.GSR.GNFS.CD%22%2C%22BN.KLT.DINV.CD%22%2C%22BX.KLT.DINV.WD.GD.ZS%22%2C%22BX.TRF.PWKR.DT.GD.ZS%22%2C%22CM.MKT.TRAD.GD.ZS%22%2C%22DT.TDS.DPPF.XP.ZS%22%2C%22EG.CFT.ACCS.ZS%22%2C%22EG.ELC.ACCS.RU.ZS%22%2C%22EG.ELC.ACCS.UR.ZS%22%2C%22EG.ELC.ACCS.ZS%22%2C%22EG.ELC.RNWX.ZS%22%2C%22EG.FEC.RNEW.ZS%22%2C%22EG.USE.COMM.CL.ZS%22%2C%22EG.USE.ELEC.KH.PC%22%2C%22EN.ATM.CO2E.PC%22%2C%22EN.ATM.GHGT.KT.CE%22%2C%22EN.ATM.PM25.MC.ZS%22%2C%22EN.CLC.DRSK.XQ%22%2C%22EN.CLC.MDAT.ZS%22%2C%22EN.CO2.TRAN.ZS%22%2C%22EN.POP.SLUM.UR.ZS%22%2C%22ER.FSH.AQUA.MT%22%2C%22ER.FSH.CAPT.MT%22%2C%22ER.FSH.PROD.MT%22%2C%22ER.H2O.FWST.ZS%22%2C%22ER.H2O.FWTL.ZS%22%2C%22ER.LND.PTLD.ZS%22%2C%22ER.MRN.PTMR.ZS%22%2C%22ER.PTD.TOTL.ZS%22%2C%22FP.CPI.TOTL.ZG%22%2C%22FX.OWN.TOTL.ZS%22%2C%22GB.XPD.RSDV.GD.ZS%22%2C%22GC.DOD.TOTL.GD.ZS%22%2C%22GC.REV.SOCL.ZS%22%2C%22GC.TAX.TOTL.GD.ZS%22%2C%22GF.XPD.BUDG.ZS%22%2C%22HD.HCI.OVRL%22%2C%22IC.FRM.BNKS.ZS%22%2C%22IC.FRM.BRIB.ZS%22%2C%22IC.FRM.FEMM.ZS%22%2C%22IE.PPN.ENGY.CD%22%2C%22IE.PPN.TRAN.CD%22%2C%22IE.PPN.WATR.CD%22%2C%22IQ.SPI.OVRL%22%2C%22IS.RRS.GOOD.MT.K6%22%2C%22IS.RRS.PASG.KM%22%2C%22IT.CEL.SETS.P2%22%2C%22IT.NET.BBND.P2%22%2C%22IT.NET.USER.ZS%22%2C%22LP.LPI.ITRN.XQ%22%2C%22MS.MIL.TOTL.TF.ZS%22%2C%22MS.MIL.XPND.GD.ZS%22%2C%22NE.EXP.GNFS.ZS%22%2C%22NV.AGR.TOTL.ZS%22%2C%22NV.IND.MANF.ZS%22%2C%22NY.ADJ.DFOR.GN.ZS%22%2C%22NY.ADJ.SVNX.GN.ZS%22%2C%22NY.GDP.MKTP.CD%22%2C%22NY.GDP.MKTP.CN%22%2C%22NY.GDP.MKTP.KD%22%2C%22NY.GDP.MKTP.KD.ZG%22%2C%22NY.GDP.MKTP.KN%22%2C%22NY.GDP.PCAP.CD%22%2C%22NY.GDP.PCAP.CN%22%2C%22NY.GDP.PCAP.KD%22%2C%22NY.GDP.PCAP.KD.ZG%22%2C%22NY.GDP.PCAP.KN%22%2C%22NY.GDP.TOTL.RT.ZS%22%2C%22NY.GNP.MKTP.CD%22%2C%22NY.GNP.MKTP.CN%22%2C%22NY.GNP.MKTP.KD%22%2C%22NY.GNP.MKTP.KN%22%2C%22NY.GNP.PCAP.KD.ZG%22%2C%22SE.ADT.1524.LT.ZS%22%2C%22SE.ADT.LITR.ZS%22%2C%22SE.ENR.PRSC.FM.ZS%22%2C%22SE.PRM.CMPT.ZS%22%2C%22SE.PRM.ENRR%22%2C%22SE.SEC.CMPT.LO.FE.ZS%22%2C%22SE.SEC.CMPT.LO.MA.ZS%22%2C%22SE.SEC.CMPT.LO.ZS%22%2C%22SE.XPD.TOTL.GB.ZS%22%2C%22SG.GEN.PARL.ZS%22%2C%22SG.LAW.INDX%22%2C%22SH.DYN.AIDS.ZS%22%2C%22SH.DYN.MORT%22%2C%22SH.DYN.MORT.FE%22%2C%22SH.DYN.MORT.MA%22%2C%22SH.H2O.BASW.ZS%22%2C%22SH.H2O.SMDW.ZS%22%2C%22SH.HIV.INCD.ZS%22%2C%22SH.IMM.MEAS%22%2C%22SH.SGR.CRSK.ZS%22%2C%22SH.STA.BASS.ZS%22%2C%22SH.STA.HYGN.ZS%22%2C%22SH.STA.MMRT%22%2C%22SH.STA.SMSS.ZS%22%2C%22SH.STA.STNT.FE.ZS%22%2C%22SH.STA.STNT.MA.ZS%22%2C%22SH.STA.STNT.ZS%22%2C%22SH.STA.TRAF.P5%22%2C%22SI.DST.50MD%22%2C%22SI.DST.FRST.20%22%2C%22SI.POV.DDAY%22%2C%22SI.POV.GINI%22%2C%22SI.POV.MDIM%22%2C%22SI.POV.NAHC%22%2C%22SI.RMT.COST.IB.ZS%22%2C%22SI.RMT.COST.OB.ZS%22%2C%22SI.SPR.PC40.ZG%22%2C%22SI.SPR.PCAP.ZG%22%2C%22SL.EMP.SMGT.FE.ZS%22%2C%22SL.EMP.TOTL.SP.ZS%22%2C%22SL.FAM.0714.ZS%22%2C%22SL.GDP.PCAP.EM.KD%22%2C%22SL.TLF.0714.ZS%22%2C%22SL.TLF.CACT.ZS%22%2C%22SL.UEM.TOTL.ZS%22%2C%22SM.POP.NETM%22%2C%22SM.POP.REFG%22%2C%22SN.ITK.DEFC.ZS%22%2C%22SN.ITK.SVFI.ZS%22%2C%22SP.ADO.TFRT%22%2C%22SP.DYN.CONU.ZS%22%2C%22SP.DYN.LE00.IN%22%2C%22SP.POP.GROW%22%2C%22SP.POP.TOTL%22%2C%22SP.REG.BRTH.RU.ZS%22%2C%22SP.REG.BRTH.UR.ZS%22%2C%22SP.REG.BRTH.ZS%22%2C%22SP.URB.GROW%22%2C%22SP.URB.TOTL.IN.ZS%22%2C%22TX.VAL.TECH.MF.ZS%22%2C%22VC.IDP.NWDS%22%2C%22VC.IHR.PSRC.P5%22%2C%22per_allsp.cov_pop_tot%22%5D%2C%5B%22License_Type%22%2C%22License_URL%22%2C%22WDITable%22%2C%22decimal%22%2C%22description%22%2C%22en%22%2C%22fullname%22%2C%22id%22%2C%22last_year%22%2C%22relatedIndicators%22%2C%22shortname%22%2C%22source%22%2C%22sourceNote%22%2C%22sourceOrganization%22%2C%22sourceURL%22%2C%22topics%22%2C%22unit%22%5D%5D%5D&method=get",
    'projects_and_operations_data': "https://data.worldbank.org/model.json?paths=%5B%5B%22extraData%22%2C%5B%22climate%22%2C%22finances%22%2C%22human_capital_index%22%2C%22projects%22%2C%22prospects%22%2C%22subnational%22%2C%22surveys%22%2C%22templateUrls%22%5D%2C%22{sort_name}%22%5D%5D&method=get",
    'other_indecators_data':"https://data.worldbank.org/model.json?paths=%5B%5B%22extraData%22%2C%5B%22climate%22%2C%22finances%22%2C%22human_capital_index%22%2C%22projects%22%2C%22prospects%22%2C%22subnational%22%2C%22surveys%22%2C%22templateUrls%22%5D%2C%22{sort_name}%22%5D%5D&method=get",
    'list_of_projects':"https://search.worldbank.org/api/v3/projects?format=json&fct=projectfinancialtype_exact,status_exact,countryshortname_exact,sector_exact,theme_exact,regionname_exact,fiscalyear&fl=id,status,project_name,countryshortname,boardapprovaldate,totalcommamt_srt,countrycode,regionname&statsfield=totalamt,totalcommamt_srt&statsfacet=countryshortname_exact^regionname_exact^fiscalyear&rows=6&os=0&srt=boardapprovaldate&order=desc&apilang=en&status_exact=Active^Closed&prodline_exact=GU^PE&countrycode_exact={sort_name}&os=0",

}

def get_url(link_type: str, sort_name: str) -> str:
    """
    Generate a URL based on the link type and sort name.
    :param link_type: The type of link to generate (e.g., 'sectors', 'projects_and_operations')
    :param sort_name: The sort name to be inserted into the URL
    :return: The generated URL
    """
    if link_type not in LINK_TEMPLATES:
        raise ValueError(f"Unknown link type: {link_type}")
    
    return LINK_TEMPLATES[link_type].format(sort_name=sort_name)
