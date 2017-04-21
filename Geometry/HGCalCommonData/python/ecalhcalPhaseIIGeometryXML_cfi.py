import FWCore.ParameterSet.Config as cms

XMLIdealGeometryESSource = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring('Geometry/CMSCommonData/data/materials.xml', 
        'Geometry/HcalCommonData/data/average/hcalforwardmaterial.xml',
        'Geometry/TrackerCommonData/data/trackermaterial.xml',
        'Geometry/CMSCommonData/data/rotations.xml', 
        "Geometry/HcalCommonData/data/hcalrotations.xml",
        'Geometry/CMSCommonData/data/normal/cmsextent.xml', 
        'Geometry/CMSCommonData/data/cms.xml', 
        'Geometry/CMSCommonData/data/cmsMother.xml',
        'Geometry/CMSCommonData/data/eta3/etaMax.xml',
        'Geometry/CMSCommonData/data/caloBase/2023/v1/caloBase.xml', 
        'Geometry/CMSCommonData/data/cmsCalo.xml', 
        'Geometry/CMSCommonData/data/muonBase.xml', 
        'Geometry/CMSCommonData/data/cmsMuon.xml', 
        'Geometry/CMSCommonData/data/mgnt.xml', 
        'Geometry/CMSCommonData/data/muonMB.xml', 
        'Geometry/CMSCommonData/data/muonMagnet.xml', 
        'Geometry/EcalCommonData/data/PhaseII/eregalgo.xml',
        'Geometry/EcalCommonData/data/ebalgo.xml',
        'Geometry/EcalCommonData/data/ebcon.xml',
        'Geometry/EcalCommonData/data/ebrot.xml',
        'Geometry/EcalCommonData/data/eecon.xml',
        'Geometry/EcalCommonData/data/ectkcable.xml',
        'Geometry/EcalCommonData/data/PhaseII/esalgo.xml',
        'Geometry/EcalCommonData/data/PhaseII/escon.xml',
        'Geometry/HcalCommonData/data/hcalrotations.xml',
        'Geometry/HcalCommonData/data/PhaseII/HGCal/hcalalgo.xml',
        'Geometry/HcalCommonData/data/PhaseII/HGCal/hcalendcapalgo.xml',
        'Geometry/HcalCommonData/data/hcalcablealgo.xml',
        'Geometry/HcalCommonData/data/hcalbarrelalgo.xml',
        'Geometry/HcalCommonData/data/hcalouteralgo.xml',
        'Geometry/HcalCommonData/data/hcalforwardalgo.xml',
        'Geometry/HcalCommonData/data/hcalforwardfibre.xml',
        'Geometry/HcalCommonData/data/hcalforwardmaterial.xml',
        'Geometry/HGCalCommonData/data/hgcal/v6/hgcal.xml',
        'Geometry/HGCalCommonData/data/hgcalEE/v5/hgcalEE.xml',
        'Geometry/HGCalCommonData/data/hgcalHEsil/v6/hgcalHEsil.xml',
        'Geometry/HGCalCommonData/data/hgcalCons/v6/hgcalCons.xml',
        'Geometry/ForwardCommonData/data/v2/forwardshield.xml',
        'Geometry/ForwardCommonData/data/forward.xml',
        'Geometry/HcalSimData/data/CaloUtil.xml',
        'Geometry/EcalSimData/data/PhaseII/ecalsens.xml', 
        'Geometry/HcalCommonData/data/PhaseII/HGCal/hcalsenspmf.xml',
        'Geometry/HcalCommonData/data/PhaseII/HGCal/hcalSimNumbering.xml',
        'Geometry/HcalCommonData/data/PhaseII/HGCal/hcalRecNumbering.xml',
        'Geometry/HcalSimData/data/hf.xml',
        'Geometry/HcalSimData/data/hfpmt.xml',
        'Geometry/HcalSimData/data/hffibrebundle.xml',
        'Geometry/HGCalSimData/data/hgcsensv6.xml', 
        'Geometry/HGCalSimData/data/hgccons.xml', 
        'Geometry/HcalSimData/data/HcalProdCuts.xml',
        'Geometry/EcalSimData/data/EcalProdCuts.xml',
        'Geometry/HGCalSimData/data/hgcProdCuts.xml', 
        'Geometry/CMSCommonData/data/FieldParameters.xml'),
    rootNodeName = cms.string('cms:OCMS')
)


