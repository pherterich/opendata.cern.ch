# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2012, 2013, 2014 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

from fixture import DataSet
#from invenio.modules.search.fixtures import FormatData
from invenio.modules.search import fixtures as default

class CollectionData(DataSet):

    siteCollection = default.CollectionData.siteCollection

    class CMS(siteCollection):
        id = 2
        name = 'CMS'
        dbquery = None

    class CMSPrimaryDataset(siteCollection):
        id = 3
        name = 'CMS Primary Dataset'
        dbquery = '980__a:"CMSPRIMARYDATASET"'

    class CMSDerivedDataset(siteCollection):
        id = 4
        name = 'CMS Derived Dataset'
        dbquery = '980__a:"CMSDERIVEDDATASET"'

    class ALICE(siteCollection):
        id = 5
        name = 'ALICE'
        dbquery = None

    class ALICESimplifiedDataset(siteCollection):
        id = 6
        name = 'ALICE Simplified Dataset'
        dbquery = '980__a:"ALICESIMPLIFIEDDATASET"'

    class ALICEAnalysis(siteCollection):
        id = 7
        name = 'ALICE Analysis'
        dbquery = '980__a:"ALICEANALYSIS"'

    class CMSTools(siteCollection):
        id = 8
        name = 'CMS Tools'
        dbquery = '980__a:"CMSTOOL"'


class CollectionCollectionData(DataSet):

    class siteCollection_CMS:
        dad = CollectionData.siteCollection
        son = CollectionData.CMS
        score = 0
        type = 'r'

    class CMS_CMSPrimaryDataset:
        dad = CollectionData.CMS
        son = CollectionData.CMSPrimaryDataset
        score = 0
        type = 'r'

    class CMS_CMSDerivedDataset:
        dad = CollectionData.CMS
        son = CollectionData.CMSDerivedDataset
        score = 1
        type = 'r'

    class CMS_CMSTools:
        dad = CollectionData.CMS
        son = CollectionData.CMSTools
        score = 2
        type = 'r'

    class siteCollection_ALICE:
        dad = CollectionData.siteCollection
        son = CollectionData.ALICE
        score = 1
        type = 'r'

    class ALICE_ALICESimplifiedDataset:
        dad = CollectionData.ALICE
        son = CollectionData.ALICESimplifiedDataset
        score = 0
        type = 'r'

    class ALICE_ALICEAnalysis:
        dad = CollectionData.ALICE
        son = CollectionData.ALICEAnalysis
        score = 1
        type = 'r'


class CollectiondetailedrecordpagetabsData(DataSet):

    class Collectiondetailedrecordpagetabs_1:
        tabs = u'metadata;files'
        id_collection = CollectionData.siteCollection.ref('id')


class CollectionFormatData(DataSet):

    class CollectionFormat_1_1:
        score = 100
        id_format = 1 # FormatData.Format_1.ref('id')
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionFormat_1_2:
        score = 90
        id_format = 2 # FormatData.Format_2.ref('id')
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionFormat_1_3:
        score = 80
        id_format = 3 # FormatData.Format_3.ref('id')
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionFormat_1_4:
        score = 70
        id_format = 4 # FormatData.Format_4.ref('id')
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionFormat_1_5:
        score = 60
        id_format = 5 # FormatData.Format_5.ref('id')
        id_collection = CollectionData.siteCollection.ref('id')


class PortalboxData(DataSet):

    class Portalbox_1:
        body = u'The <b>CMS</b> (Compact Muon Solenoid) experiment is one of two large general-purpose particle physics detectors built on the Large Hadron Collider (LHC) at CERN in Switzerland and France. The goal of CMS experiment is to investigate a wide range of physics, including the search for the Higgs boson, extra dimensions, and particles that could make up dark matter.'
        id = 1
        title = u'description'

    class Portalbox_2:
        body = u'CMS.gif'
        id = 2
        title = u'image'

    class Portalbox_3:
        body = u'ALICE (A Large Ion Collider Experiment) is one of seven detector experiments at the Large Hadron Collider at CERN. The other six are: ATLAS, CMS, TOTEM, LHCb, LHCf and MoEDAL. ALICE is optimized to study heavy-ion (Pb-Pb nuclei) collisions at a centre of mass energy of 2.76 TeV per nucleon pair. The resulting temperature and energy density are expected to be high enough to produce quark–gluon plasma, a state of matter wherein quarks and gluons are freed. Similar conditions are believed to existed a fraction of the second after the Big Bang before quarks and gluons bound together to form hadrons and heavier particles.'
        id = 3
        title = u'description'

    class Portalbox_4:
        body = u'ALICE.gif'
        id = 4
        title = u'image'

    class Portalbox_5:
        body = u'CMS Primary Dataset.CMS Primary Dataset.CMS Primary Dataset.CMS Primary Dataset.CMS Primary Dataset.CMS Primary Dataset.CMS Primary Dataset.CMS Primary Dataset.CMS Primary Dataset.CMS Primary Dataset'
        id = 5
        title = u'description'

    class Portalbox_6:
        body = u'default.png'
        id = 6
        title = u'image'

    class Portalbox_7:
        body = u'CMS Derived Dataset.CMS Derived Dataset.CMS Derived Dataset.CMS Derived Dataset.CMS Derived Dataset.CMS Derived Dataset.CMS Derived Dataset.CMS Derived Dataset.CMS Derived Dataset.CMS Derived Dataset'
        id = 7
        title = u'description'

    class Portalbox_8:
        body = u'default.png'
        id = 8
        title = u'image'

    class Portalbox_9:
        body = u'ALICE Simplified Dataset.ALICE Simplified Dataset.ALICE Simplified Dataset.ALICE Simplified Dataset.ALICE Simplified Dataset.ALICE Simplified Dataset.ALICE Simplified Dataset.ALICE Simplified Dataset.ALICE Simplified Dataset.ALICE Simplified Dataset'
        id = 9
        title = u'description'

    class Portalbox_10:
        body = u'default.png'
        id = 10
        title = u'image'

    class Portalbox_11:
        body = u'ALICE Analysis.ALICE Analysis.ALICE Analysis.ALICE Analysis.ALICE Analysis.ALICE Analysis.ALICE Analysis.ALICE Analysis.ALICE Analysis.ALICE Analysis'
        id = 11
        title = u'description'

    class Portalbox_12:
        body = u'default.png'
        id = 12
        title = u'image'


class CollectionPortalboxData(DataSet):

    class CollectionPortalbox_2_1_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_1.ref('id')
        score = 100
        id_collection = CollectionData.CMS.ref('id')

    class CollectionPortalbox_2_2_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_2.ref('id')
        score = 100
        id_collection = CollectionData.CMS.ref('id')

    class CollectionPortalbox_5_3_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_3.ref('id')
        score = 100
        id_collection = CollectionData.ALICE.ref('id')

    class CollectionPortalbox_5_4_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_4.ref('id')
        score = 100
        id_collection = CollectionData.ALICE.ref('id')

    class CollectionPortalbox_3_5_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_5.ref('id')
        score = 100
        id_collection = CollectionData.CMSPrimaryDataset.ref('id')

    class CollectionPortalbox_3_6_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_6.ref('id')
        score = 100
        id_collection = CollectionData.CMSPrimaryDataset.ref('id')

    class CollectionPortalbox_4_7_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_7.ref('id')
        score = 100
        id_collection = CollectionData.CMSDerivedDataset.ref('id')

    class CollectionPortalbox_4_8_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_8.ref('id')
        score = 100
        id_collection = CollectionData.CMSDerivedDataset.ref('id')

    class CollectionPortalbox_6_9_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_9.ref('id')
        score = 100
        id_collection = CollectionData.ALICEAnalysis.ref('id')

    class CollectionPortalbox_6_10_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_10.ref('id')
        score = 100
        id_collection = CollectionData.ALICEAnalysis.ref('id')

    class CollectionPortalbox_7_11_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_11.ref('id')
        score = 100
        id_collection = CollectionData.ALICESimplifiedDataset.ref('id')

    class CollectionPortalbox_7_12_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_12.ref('id')
        score = 100
        id_collection = CollectionData.ALICESimplifiedDataset.ref('id')


__all__ = (
    'CollectionData',
    'CollectionCollectionData',
    'CollectiondetailedrecordpagetabsData',
    'CollectionFormatData',
    'PortalboxData',
    'CollectionPortalboxData',
)
