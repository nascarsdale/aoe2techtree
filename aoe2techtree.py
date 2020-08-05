def return_all_units():
    all_units = {
        'barracks':
            {
            'swords':
               [
                    'militia',
                    'man-at-arms',
                    'longswordsman',
                    'two-handed swordsman',
                    'champion'
                ],
            'spears':
                [
                    'spear',
                    'pikeman',
                    'halberdier'
                ],
            'eagles':
                [
                    'eagle scout',
                    'eagle warrior',
                    'elite eagle warrior'
                ]
            },
        'archery range':
            {
            'archers':
                [
                    'archer',
                    'crossbow',
                    'arbalest'
                ],
            'skirmisher':
                [
                    'skirmisher',
                    'elite skirmisher'
                ],
            'cavalry archer':
                [
                    'cavalry archer',
                    'heavy cavalry archer'
                ],
            'hand cannon':
                [
                    'hand cannon'    
                ]
            },
        'stable':
            {
                'light cavalry':
                    [
                        'scout',
                        'light cavalry',
                        'hussar'
                    ],
                'knight':
                    [
                        'knight',
                        'cavalier',
                        'paladin'
                    ],
                'camel':
                    [
                        'camel',
                        'heavy camel',
                    ],
                'battle elephant':
                    [
                        'battle elephant',
                        'elite battle elephant'
                    ]
            },
        'siege workshop':
            {
                'mangonel':
                    [
                        'mangonel',
                        'onager',
                        'siege onager'
                    ],
                'ram':
                    [
                        'battering ram',
                        'capped ram',
                        'siege ram'
                    ],
                'scorpion':
                    [
                        'scorpion',
                        'heavy scorpion'
                    ],
                'bombard cannon':
                    [
                        'bombard cannon'    
                    ]
            },
        'dock':
            {
                'galley':
                    [
                        'galley',
                        'war galley',
                        'galleon'
                    ],
                'fire ship':
                    [
                        'fire raft',
                        'fire ship',
                        'fast fire ship'
                    ],
                'demo ship':
                    [
                        'demo raft',
                        'demo ship',
                        'heavy demo ship'
                    ],
                'cannon galleon':
                    [
                        'cannon galleon',
                        'elite cannon galleon'
                    ]
            },
        'techs':
            {
                'techslist':
                    [
                        'arson',
                        'squires',
                        'thumb ring',
                        'parthian tactics',
                        'bloodlines',
                        'husbandry',
                        'archer armor 1',
                        'archer armor 2',
                        'archer armor 3',
                        'fletching',
                        'bodkin arrow',
                        'bracer',
                        'melee attack 1',
                        'melee attack 2',
                        'melee attack 3',
                        'cavalry armor 1',
                        'cavalry armor 2',
                        'cavalry armor 3',
                        'infantry armor 1',
                        'infantry armor 2',
                        'infantry armor 3',
                        'full blacksmith',
                        #dock
                        'careening', 
                        'dry dock', 
                        'shipwright', 
                        #univesity
                        'masonry', 
                        'architecture', 
                        'stone wall', 
                        'fortified wall', 
                        'guard tower', 
                        'keep', 
                        'bombard tower',
                        'siege engineers', 
                        'heated shot',  
                        'treadmill crane', 
                        'arrowslits', 
                        #monastery
                        'redemption', 
                        'atonement', 
                        'herbal medicine', 
                        'heresy', 
                        'sanctity', 
                        'fervor', 
                        'faith', 
                        'illumination', 
                        'block printing', 
                        'theocracy', 
                        #eco techs
                        'gold 2', 
                        'stone 2', 
                        'two man saw', 
                        'guilds', 
                        'crop rotation'
                    ]
            }

        }
        
    return all_units

def civ_attributes(): 
    attributes = {
            'aztecs':
                {
                    #barracks
                    'swords' : 'full',
                    'spears' : 2,
                    'eagles' : 'full',
                    
                    #range
                    'archers': 'full',
                    'skirmisher' : 'full',
                    'cavalry archer' : 0,
                    'hand cannon': 0,
                
                    #stable
                   'light cavalry': 0,
                    'knight' : 0,
                    'camel' : 0,
                    'battle elephant' : 0,
                
                    #workshop
                   'ram' : 'full',
                   'mangonel' : 'full',
                   'scorpion' : 1,
                   'bombard cannon' : 0,

                    #dock
                    'galley' : 2,
                    'fire ship' : 'full',
                    'demo ship' : 2,
                    'cannon galleon' : 0,

                    #TECHS
                    'arson'             :1, 
                    'squires'           :1, 
                    'thumb ring'        :0,
                    'parthian tactics'  :0,
                    'bloodlines'        :0,
                    'husbandry'         :0,
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :0,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :0,
                    'cavalry armor 2'   :0,
                    'cavalry armor 3'   :0,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :0,
                    #dock
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :1,
                    #univesity
                    'masonry'           :0,
                    'architecture'      :0,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :0,
                    'bombard tower'     :0,
                    'siege engineers'   :1,     
                    'heated shot'       :1,
                    'treadmill crane'   :1,
                    'arrowslits'        :1,
                    #monastery
                    'redemption'        :1,
                    'atonement'         :1,
                    'herbal medicine'   :1,
                    'heresy'            :1,
                    'sanctity'          :1,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :1,
                    'block printing'    :1,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :1,
                    'stone 2'           :1,
                    'two man saw'       :0,
                    'guilds'            :0,
                    'crop rotation'     :1,
                    'techslist': None

                },

            'berbers':
                {
                    #barracks
                    'swords' : 'full',
                    'spears' : 2,
                    'eagles' : 0,

                    #range
                    'archers': 2,
                    'skirmisher' : 'full',
                    'cavalry archer' : 'full',
                    'hand cannon': 1,

                    #stable
                   'light cavalry': 'full',
                    'knight' : 2,
                    'camel' : 'full',
                    'battle elephant' : 0,

                    #workshop
                   'ram' : 2,
                   'mangonel' : 2,
                   'scorpion' : 'full',
                   'bombard cannon' : 1,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 'full',
                    'demo ship' : 'full',
                    'cannon galleon' : 'full',

                    'arson'             :1,
                    'squires'           :1,
                    'thumb ring'        :1,
                    'parthian tactics'  :0,
                    'bloodlines'        :1,
                    'husbandry'         :1,
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :1,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :1,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :1,
                    #dock
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :0,
                    #univesity
                    'masonry'           :1,
                    'architecture'      :0,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :0,
                    'bombard tower'     :0,
                    'siege engineers'   :1,
                    'heated shot'       :1,
                    'treadmill crane'   :1,
                    'arrowslits'        :1,
                    #monastery
                    'redemption'        :1,
                    'atonement'         :1,
                    'herbal medicine'   :1,
                    'heresy'            :1,
                    'sanctity'          :0,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :1,
                    'block printing'    :0,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :1,
                    'stone 2'           :1,
                    'two man saw'       :0,
                    'guilds'            :1,
                    'crop rotation'     :1,
                    'techslist': None

                },

            'britons':
                {
                    #barracks
                    'swords' : 'full',
                    'spears' : 'full',
                    'eagles' : 0,

                    #range
                    'archers': 'full',
                    'skirmisher' : 'full',
                    'cavalry archer' : 'full',
                    'hand cannon': 0,

                    #stable
                   'light cavalry': 2,
                    'knight' : 2,
                    'camel' : 0,
                    'battle elephant' : 0,

                    #workshop
                   'ram' : 2,
                   'mangonel' : 2,
                   'scorpion' : 'full',
                   'bombard cannon' : 0,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 'full',
                    'demo ship' : 'full',
                    'cannon galleon' : 1,

                    'arson'             :1,
                    'squires'           :1,
                    'thumb ring'        :0,
                    'parthian tactics'  :0,
                    'bloodlines'        :0,
                    'husbandry'         :1,
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :1,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :1,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :1,
                    #dock
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :1,
                    #univesity
                    'masonry'           :1,
                    'architecture'      :1,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :1,
                    'bombard tower'     :0,
                    'siege engineers'   :1,
                    'heated shot'       :1,
                    'treadmill crane'   :0,
                    'arrowslits'        :1,
                    #monastery
                    'redemption'        :0,
                    'atonement'         :0,
                    'herbal medicine'   :1,
                    'heresy'            :0,
                    'sanctity'          :1,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :1,
                    'block printing'    :1,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :1,
                    'stone 2'           :0,
                    'two man saw'       :1,
                    'guilds'            :1,
                    'crop rotation'     :0,
                    'techslist': None
                },

            'burmese':
                {
                    #barracks
                    'swords' : 'full',
                    'spears' : 'full',
                    'eagles' : 0,

                    #range
                    'archers': 2,
                    'skirmisher' : 'full',
                    'cavalry archer' : 'full',
                    'hand cannon': 0,

                    #stable
                   'light cavalry': 'full',
                    'knight' : 2,
                    'camel' : 0,
                    'battle elephant' : 'full',

                    #workshop
                   'ram' : 2,
                   'mangonel' : 2,
                   'scorpion' : 'full',
                   'bombard cannon' : 1,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 2,
                    'demo ship' : 2,
                    'cannon galleon' : 'full',

                    'arson'             :1,
                    'squires'           :1,
                    'thumb ring'        :0,
                    'parthian tactics'  :1,
                    'bloodlines'        :1,
                    'husbandry'         :1,
                    'archer armor 1'    :1,
                    'archer armor 2'    :0,
                    'archer armor 3'    :0,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :1,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :0,
                    #dock
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :0,
                    #univesity
                    'masonry'           :1,
                    'architecture'      :1,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :1,
                    'bombard tower'     :0,
                    'siege engineers'   :1,
                    'heated shot'       :1,
                    'treadmill crane'   :1,
                    'arrowslits'        :0,
                    #monastery
                    'redemption'        :1,
                    'atonement'         :1,
                    'herbal medicine'   :1,
                    'heresy'            :0,
                    'sanctity'          :1,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :1,
                    'block printing'    :1,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :1,
                    'stone 2'           :0,
                    'two man saw'       :1,
                    'guilds'            :1,
                    'crop rotation'     :1,
                    #troubleshooting
                    'techslist': None
                }, 
        
            'byzantines':
                {
                    
                    #range
                    'archers': 'full',
                    'skirmisher' : 'full',
                    'cavalry archer' : 'full',
                    'hand cannon' : 1,
                    #techs
                    'thumb ring'        :1,
                    'parthian tactics'  :0,
                    
                    #barracks
                    'swords' : 'full',
                    'spears' : 'full',
                    'eagles' : 0,
                    #techs
                    'arson'             :1, 
                    'squires'           :1, 

                    #stable
                   'light cavalry': 'full',
                    'knight' : 'full',
                    'camel' : 'full',
                    'battle elephant' : 0,
                    #techs
                    'bloodlines'        :0,
                    'husbandry'         :1,
                
                    #workshop
                   'ram' : 'full',
                   'mangonel' : 2,
                   'scorpion' : 1,
                   'bombard cannon' : 1,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :1,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :0,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :1,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :0,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 'full',
                    'demo ship' : 'full',
                    'cannon galleon' : 'full',
                    #techs
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :1,

                    #university
                    'masonry'           :0,
                    'architecture'      :0,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :1,
                    'bombard tower'     :1,
                    'siege engineers'   :0,     
                    'heated shot'       :0,
                    'treadmill crane'   :0,
                    'arrowslits'        :1,
                    
                    #monastery
                    'redemption'        :1,
                    'atonement'         :1,
                    'herbal medicine'   :0,
                    'heresy'            :1,
                    'sanctity'          :1,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :1,
                    'block printing'    :1,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :1,
                    'stone 2'           :1,
                    'two man saw'       :1,
                    'guilds'            :1,
                    'crop rotation'     :1,
                    'techslist': None

                },

        'celts':
                {
                    
                    #range
                    'archers': 2,
                    'skirmisher' : 'full',
                    'cavalry archer' : 'full',
                    'hand cannon' : 0,
                    #techs
                    'thumb ring'        :0,
                    'parthian tactics'  :0,
                    
                    #barracks
                    'swords' : 'full',
                    'spears' : 'full',
                    'eagles' : 0,
                    #techs
                    'arson'             :1, 
                    'squires'           :0, 

                    #stable
                   'light cavalry': 'full',
                    'knight' : 'full',
                    'camel' : 0,
                    'battle elephant' : 0,
                    #techs
                    'bloodlines'        :0,
                    'husbandry'         :1,
                
                    #workshop
                   'ram' : 'full',
                   'mangonel' : 'full',
                   'scorpion' : 'full',
                   'bombard cannon' : 0,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :0,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :0,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :0,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :0,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 2,
                    'demo ship' : 'full',
                    'cannon galleon' : 1,
                    #techs
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :1,

                    #university
                    'masonry'           :1,
                    'architecture'      :0,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :1,
                    'bombard tower'     :0,
                    'siege engineers'   :1,     
                    'heated shot'       :1,
                    'treadmill crane'   :1,
                    'arrowslits'        :1,
                    
                    #monastery
                    'redemption'        :0,
                    'atonement'         :0,
                    'herbal medicine'   :1,
                    'heresy'            :1,
                    'sanctity'          :1,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :0,
                    'block printing'    :0,
                    'theocracy'         :0,
                    #eco techs
                    'gold 2'            :1,
                    'stone 2'           :1,
                    'two man saw'       :0,
                    'guilds'            :1,
                    'crop rotation'     :0,
                    'techslist': None

                }, 
        
        'chinese':
                {
                    
                    #range
                    'archers': 'full',
                    'skirmisher' : 'full',
                    'cavalry archer' : 'full',
                    'hand cannon' : 0,
                    #techs
                    'thumb ring'        :1,
                    'parthian tactics'  :0,
                    
                    #barracks
                    'swords' : 'full',
                    'spears' : 'full',
                    'eagles' : 0,
                    #techs
                    'arson'             :1, 
                    'squires'           :1, 

                    #stable
                   'light cavalry': 2,
                    'knight' : 2,
                    'camel' : 'full',
                    'battle elephant' : 0,
                    #techs
                    'bloodlines'        :1,
                    'husbandry'         :1,
                
                    #workshop
                   'ram' : 'full',
                   'mangonel' : 2,
                   'scorpion' : 'full',
                   'bombard cannon' : 0,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :1,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :1,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :1,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 2,
                    'demo ship' : 'full',
                    'cannon galleon' : 1,
                    #techs
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :1,

                    #university
                    'masonry'           :1,
                    'architecture'      :1,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :1,
                    'bombard tower'     :1,
                    'siege engineers'   :0,     
                    'heated shot'       :1,
                    'treadmill crane'   :0,
                    'arrowslits'        :1,
                    
                    #NOTE this is wrong for HD
                    #monastery
                    'redemption'        :0,
                    'atonement'         :1,
                    'herbal medicine'   :1,
                    'heresy'            :0,
                    'sanctity'          :1,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :1,
                    'block printing'    :1,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :1,
                    'stone 2'           :1,
                    'two man saw'       :1,
                    'guilds'            :0,
                    'crop rotation'     :0,
                    'techslist': None

                }, 
        
        'ethiopians':
                {
                    
                    #range
                    'archers': 'full',
                    'skirmisher' : 'full',
                    'cavalry archer' : 'full',
                    'hand cannon' : 0,
                    #techs
                    'thumb ring'        :1,
                    'parthian tactics'  :0,
                    
                    #barracks
                    'swords' : 4,
                    'spears' : 'full',
                    'eagles' : 0,
                    #techs
                    'arson'             :1, 
                    'squires'           :1, 

                    #stable
                   'light cavalry': 'full',
                    'knight' : 2,
                    'camel' : 'full',
                    'battle elephant' : 0,
                    #techs
                    'bloodlines'        :0,
                    'husbandry'         :1,
                
                    #workshop
                   'ram' : 'full',
                   'mangonel' : 'full',
                   'scorpion' : 'full',
                   'bombard cannon' : 1,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :1,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :0,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :0,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 2,
                    'demo ship' : 2,
                    'cannon galleon' : 1,
                    #techs
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :1,

                    #university
                    'masonry'           :1,
                    'architecture'      :1,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :1,
                    'bombard tower'     :0,
                    'siege engineers'   :1,     
                    'heated shot'       :1,
                    'treadmill crane'   :0,
                    'arrowslits'        :0,
                    
                    #monastery
                    'redemption'        :0,
                    'atonement'         :1,
                    'herbal medicine'   :1,
                    'heresy'            :1,
                    'sanctity'          :1,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :1,
                    'block printing'    :0,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :1,
                    'stone 2'           :1,
                    'two man saw'       :1,
                    'guilds'            :1,
                    'crop rotation'     :0,
                    'techslist': None

                }, 
        'franks':
                {
                    
                    #range
                    'archers': 2,
                    'skirmisher' : 'full',
                    'cavalry archer' : 'full',
                    'hand cannon' : 1,
                    #techs
                    'thumb ring'        :0,
                    'parthian tactics'  :0,
                    
                    #barracks
                    'swords' : 'full',
                    'spears' : 'full',
                    'eagles' : 0,
                    #techs
                    'arson'             :1, 
                    'squires'           :1, 

                    #stable
                   'light cavalry': 2,
                    'knight' : 'full',
                    'camel' : 0,
                    'battle elephant' : 0,
                    #techs
                    'bloodlines'        :1, #technically not true but their bonus
                                            #approximates this and I haven't been
                                               #including civ bonuses
                    'husbandry'         :1,
                
                    #workshop
                   'ram' : 2,
                   'mangonel' : 2,
                   'scorpion' : 'full',
                   'bombard cannon' : 0,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :0,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :0,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :1,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :0,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 'full',
                    'demo ship' : 'full',
                    'cannon galleon' : 1,
                    #techs
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :0,

                    #university
                    'masonry'           :1,
                    'architecture'      :1,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :0,
                    'bombard tower'     :0,
                    'siege engineers'   :1,     
                    'heated shot'       :0,
                    'treadmill crane'   :1,
                    'arrowslits'        :1,
                    
                    #monastery
                    'redemption'        :0,
                    'atonement'         :0,
                    'herbal medicine'   :1,
                    'heresy'            :1,
                    'sanctity'          :1,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :1,
                    'block printing'    :1,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :1,
                    'stone 2'           :0,
                    'two man saw'       :0,
                    'guilds'            :0,
                    'crop rotation'     :1,
                    'techslist': None

                }, 
         'goths':
                {
                    
                    #range
                    'archers': 2,
                    'skirmisher' : 'full',
                    'cavalry archer' : 'full',
                    'hand cannon' : 1,
                    #techs
                    'thumb ring'        :0,
                    'parthian tactics'  :0,
                    
                    #barracks
                    'swords' : 'full',
                    'spears' : 'full',
                    'eagles' : 0,
                    #techs
                    'arson'             :1, #they effectively have arson
                    'squires'           :1, 

                    #stable
                   'light cavalry': 'full',
                    'knight' : 2,
                    'camel' : 0,
                    'battle elephant' : 0,
                    #techs
                    'bloodlines'        :1,
                    'husbandry'         :1,
                
                    #workshop
                   'ram' : 2,
                   'mangonel' : 2,
                   'scorpion' : 'full',
                   'bombard cannon' : 1,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :1,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :0,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :0,
                'full blacksmith'       :0,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 'full',
                    'demo ship' : 'full',
                    'cannon galleon' : 1,
                    #techs
                    'careening'         :1,
                    'dry dock'          :0,
                    'shipwright'        :1,

                    #university
                    'masonry'           :1,
                    'architecture'      :1,
                    'stone wall'        :0,
                    'fortified wall'    :0,
                    'guard tower'       :0,
                    'keep'              :0,
                    'bombard tower'     :0,
                    'siege engineers'   :0,     
                    'heated shot'       :1,
                    'treadmill crane'   :0,
                    'arrowslits'        :0,
                    
                    #monastery
                    'redemption'        :0,
                    'atonement'         :0,
                    'herbal medicine'   :1,
                    'heresy'            :0,
                    'sanctity'          :1,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :1,
                    'block printing'    :0,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :0,
                    'stone 2'           :1,
                    'two man saw'       :1,
                    'guilds'            :1,
                    'crop rotation'     :1,
                    'techslist': None

                }, 
        'huns':
                {
                    
                    #range
                    'archers': 2,
                    'skirmisher' : 'full',
                    'cavalry archer' : 'full',
                    'hand cannon' : 0,
                    #techs
                    'thumb ring'        :1,
                    'parthian tactics'  :1,
                    
                    #barracks
                    'swords' : 4,
                    'spears' : 'full',
                    'eagles' : 0,
                    #techs
                    'arson'             :1, 
                    'squires'           :1, 

                    #stable
                   'light cavalry': 'full',
                    'knight' : 'full',
                    'camel' : 0,
                    'battle elephant' : 0,
                    #techs
                    'bloodlines'        :1,
                    'husbandry'         :1,
                
                    #workshop
                   'ram' : 'full',
                   'mangonel' : 1,
                   'scorpion' : 1,
                   'bombard cannon' : 0,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :0,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :1,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :0,
                'full blacksmith'       :0,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 2,
                    'demo ship' : 'full',
                    'cannon galleon' : 0,
                    #techs
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :0,

                    #university
                    'masonry'           :1,
                    'architecture'      :0,
                    'stone wall'        :1,
                    'fortified wall'    :0,
                    'guard tower'       :0,
                    'keep'              :0,
                    'bombard tower'     :0,
                    'siege engineers'   :0,     
                    'heated shot'       :0,
                    'treadmill crane'   :0,
                    'arrowslits'        :0,
                    
                    #monastery
                    'redemption'        :0,
                    'atonement'         :1,
                    'herbal medicine'   :0,
                    'heresy'            :1,
                    'sanctity'          :1,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :1,
                    'block printing'    :0,
                    'theocracy'         :0,
                    #eco techs
                    'gold 2'            :1,
                    'stone 2'           :0,
                    'two man saw'       :1,
                    'guilds'            :1,
                    'crop rotation'     :0,
                    'techslist': None

                }, 

        'incas':
                {
                    
                    #range
                    'archers': 'full',
                    'skirmisher' : 'full',
                    'cavalry archer' : 'full',
                    'hand cannon' : 0,
                    #techs
                    'thumb ring'        :1,
                    'parthian tactics'  :0,
                    
                    #barracks
                    'swords' : 'full',
                    'spears' : 'full',
                    'eagles' : 'full',
                    #techs
                    'arson'             :1, 
                    'squires'           :1, 

                    #stable
                   'light cavalry': 0,
                    'knight' : 0,
                    'camel' : 0,
                    'battle elephant' : 0,
                    #techs
                    'bloodlines'        :0,
                    'husbandry'         :0,
                
                    #workshop
                   'ram' : 'full',
                   'mangonel' : 2,
                   'scorpion' : 2,
                   'bombard cannon' : 0,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :1,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :0,
                    'cavalry armor 2'   :0,
                    'cavalry armor 3'   :0,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :1, #they don't get cav so all of their 
                                            #units are fully upgraded

                    #dock
                    'galley' : 'full',
                    'fire ship' : 'full',
                    'demo ship' : 2,
                    'cannon galleon' : 0,
                    #techs
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :1,

                    #university
                    'masonry'           :1,
                    'architecture'      :0,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :1,
                    'bombard tower'     :0,
                    'siege engineers'   :1,     
                    'heated shot'       :1,
                    'treadmill crane'   :1,
                    'arrowslits'        :1,
                    
                    #monastery
                    'redemption'        :1,
                    'atonement'         :0,
                    'herbal medicine'   :1,
                    'heresy'            :1,
                    'sanctity'          :1,
                    'fervor'            :0,
                    'faith'             :1,
                    'illumination'      :1,
                    'block printing'    :1,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :1,
                    'stone 2'           :1,
                    'two man saw'       :0,
                    'guilds'            :1,
                    'crop rotation'     :1,
                    'techslist': None

                }, 
                
        'indians':
                {
                    
                    #range
                    'archers': 2,
                    'skirmisher' : 'full',
                    'cavalry archer' : 'full',
                    'hand cannon' : 1,
                    #techs
                    'thumb ring'        :1,
                    'parthian tactics'  :1,
                    
                    #barracks
                    'swords' : 'full',
                    'spears' : 'full',
                    'eagles' : 0,
                    #techs
                    'arson'             :1, 
                    'squires'           :1, 

                    #stable
                   'light cavalry': 'full',
                    'knight' : 0,
                    'camel' : 'full',
                    'battle elephant' : 0,
                    #techs
                    'bloodlines'        :1,
                    'husbandry'         :1,
                
                    #workshop
                   'ram' : 2,
                   'mangonel' : 2,
                   'scorpion' : 1,
                   'bombard cannon' : 1,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :1,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :1,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :0,
                'full blacksmith'       :0,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 2,
                    'demo ship' : 'full',
                    'cannon galleon' : 2,
                    #techs
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :0,

                    #university
                    'masonry'           :1,
                    'architecture'      :0,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :0,
                    'bombard tower'     :0,
                    'siege engineers'   :1,     
                    'heated shot'       :1,
                    'treadmill crane'   :0,
                    'arrowslits'        :0,
                    
                    #monastery
                    'redemption'        :1,
                    'atonement'         :0,
                    'herbal medicine'   :1,
                    'heresy'            :0,
                    'sanctity'          :1,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :1,
                    'block printing'    :1,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :1,
                    'stone 2'           :1,
                    'two man saw'       :1,
                    'guilds'            :1,
                    'crop rotation'     :0,
                    'techslist': None

                }, 

        'italians':
                {
                    
                    #range
                    'archers': 'full',
                    'skirmisher' : 'full',
                    'cavalry archer' : 1,
                    'hand cannon' : 1,
                    #techs
                    'thumb ring'        :1,
                    'parthian tactics'  :0,
                    
                    #barracks
                    'swords' : 'full',
                    'spears' : 2,
                    'eagles' : 0,
                    #techs
                    'arson'             :1, 
                    'squires'           :1, 

                    #stable
                   'light cavalry': 'full',
                    'knight' : 2,
                    'camel' : 0,
                    'battle elephant' : 0,
                    #techs
                    'bloodlines'        :1,
                    'husbandry'         :1,
                
                    #workshop
                   'ram' : 2,
                   'mangonel' : 2,
                   'scorpion' : 1,
                   'bombard cannon' : 1,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :1,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :1,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :1,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 'full',
                    'demo ship' : 2,
                    'cannon galleon' : 2,
                    #techs
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :1,

                    #university
                    'masonry'           :1,
                    'architecture'      :1,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :1,
                    'bombard tower'     :1,
                    'siege engineers'   :0,     
                    'heated shot'       :1,
                    'treadmill crane'   :1,
                    'arrowslits'        :1,
                    
                    #monastery
                    'redemption'        :1,
                    'atonement'         :1,
                    'herbal medicine'   :1,
                    'heresy'            :0,
                    'sanctity'          :1,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :1,
                    'block printing'    :1,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :0,
                    'stone 2'           :1,
                    'two man saw'       :1,
                    'guilds'            :1,
                    'crop rotation'     :1,
                    'techslist': None

                }, 

        'japanese':
                {
                    
                    #range
                    'archers': 'full',
                    'skirmisher' : 'full',
                    'cavalry archer' : 'full',
                    'hand cannon' : 1,
                    #techs
                    'thumb ring'        :1,
                    'parthian tactics'  :1,
                    
                    #barracks
                    'swords' : 'full',
                    'spears' : 'full',
                    'eagles' : 0,
                    #techs
                    'arson'             :1, 
                    'squires'           :1, 

                    #stable
                   'light cavalry': 2,
                    'knight' : 2,
                    'camel' : 0,
                    'battle elephant' : 0,
                    #techs
                    'bloodlines'        :1, #I think this is true in expansions
                    'husbandry'         :1,
                
                    #workshop
                   'ram' : 2,
                   'mangonel' : 2,
                   'scorpion' : 'full',
                   'bombard cannon' : 0,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :1,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :0,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :0,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 'full',
                    'demo ship' : 2,
                    'cannon galleon' : 2,
                    #techs
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :1,

                    #university
                    'masonry'           :1,
                    'architecture'      :0,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :1,
                    'bombard tower'     :0,
                    'siege engineers'   :1,     
                    'heated shot'       :0,
                    'treadmill crane'   :1,
                    'arrowslits'        :1,
                    
                    #monastery
                    'redemption'        :1,
                    'atonement'         :1,
                    'herbal medicine'   :1,
                    'heresy'            :0,
                    'sanctity'          :1,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :1,
                    'block printing'    :1,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :1,
                    'stone 2'           :0,
                    'two man saw'       :1,
                    'guilds'            :0,
                    'crop rotation'     :0,
                    'techslist': None

                },
        
        'khmer':
                {
                    
                    #range
                    'archers': 'full',
                    'skirmisher' : 'full',
                    'cavalry archer' : 'full',
                    'hand cannon' : 1,
                    #techs
                    'thumb ring'        :0,
                    'parthian tactics'  :1,
                    
                    #barracks
                    'swords' : 4,
                    'spears' : 'full',
                    'eagles' : 0,
                    #techs
                    'arson'             :1, 
                    'squires'           :0, 

                    #stable
                   'light cavalry': 'full',
                    'knight' : 2,
                    'camel' : 0,
                    'battle elephant' : 2,
                    #techs
                    'bloodlines'        :1,
                    'husbandry'         :1,
                
                    #workshop
                   'ram' : 'full',
                   'mangonel' : 2,
                   'scorpion' : 2,
                   'bombard cannon' : 0,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :1,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :1,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :0,
                'full blacksmith'       :0,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 'full',
                    'demo ship' : 2,
                    'cannon galleon' : 2,
                    #techs
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :1, #not true in latest DE but in HD I 
                                            #think it is

                    #university
                    'masonry'           :1,
                    'architecture'      :1,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :1,
                    'bombard tower'     :0,
                    'siege engineers'   :1,     
                    'heated shot'       :1,
                    'treadmill crane'   :1,
                    'arrowslits'        :0,
                    
                    #monastery
                    'redemption'        :1,
                    'atonement'         :0,
                    'herbal medicine'   :1,
                    'heresy'            :0,
                    'sanctity'          :1,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :1,
                    'block printing'    :0,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :1,
                    'stone 2'           :1,
                    'two man saw'       :0,
                    'guilds'            :0,
                    'crop rotation'     :1,
                    'techslist': None

                }, 
        
        'koreans':
                {
                    
                    #range
                    'archers': 'full',
                    'skirmisher' : 'full',
                    'cavalry archer' : 'full',
                    'hand cannon' : 1,
                    #techs
                    'thumb ring'        :1,
                    'parthian tactics'  :0,
                    
                    #barracks
                    'swords' : 'full',
                    'spears' : 'full',
                    'eagles' : 0,
                    #techs
                    'arson'             :1, 
                    'squires'           :1, 

                    #stable
                   'light cavalry': 'full',
                    'knight' : 2,
                    'camel' : 0,
                    'battle elephant' : 0,
                    #techs
                    'bloodlines'        :0,
                    'husbandry'         :1,
                
                    #workshop
                   'ram' : 2,
                   'mangonel' : 'full',
                   'scorpion' : 1,
                   'bombard cannon' : 1,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :1,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :0,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :0,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :0,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 'full',
                    'demo ship' : 0,
                    'cannon galleon' : 1,
                    #techs
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :1,

                    #university
                    'masonry'           :1,
                    'architecture'      :1,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :1,
                    'bombard tower'     :1,
                    'siege engineers'   :1,     
                    'heated shot'       :1,
                    'treadmill crane'   :1,
                    'arrowslits'        :1,
                    
                    #monastery
                    'redemption'        :0,
                    'atonement'         :0,
                    'herbal medicine'   :1,
                    'heresy'            :0,
                    'sanctity'          :1,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :0,
                    'block printing'    :1,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :1,
                    'stone 2'           :1,
                    'two man saw'       :1,
                    'guilds'            :1,
                    'crop rotation'     :0,
                    'techslist': None

                }, 

        'magyars':
                {
                    
                    #range
                    'archers': 'full',
                    'skirmisher' : 'full',
                    'cavalry archer' : 'full',
                    'hand cannon' : 0,
                    #techs
                    'thumb ring'        :1,
                    'parthian tactics'  :1,
                    
                    #barracks
                    'swords' : 'full',
                    'spears' : 'full',
                    'eagles' : 0,
                    #techs
                    'arson'             :1, 
                    'squires'           :0, 

                    #stable
                   'light cavalry': 'full',
                    'knight' : 'full',
                    'camel' : 0,
                    'battle elephant' : 0,
                    #techs
                    'bloodlines'        :1,
                    'husbandry'         :1,
                
                    #workshop
                   'ram' : 2,
                   'mangonel' : 2,
                   'scorpion' : 'full',
                   'bombard cannon' : 0,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :1,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :1,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :0,
                'full blacksmith'       :0,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 'full',
                    'demo ship' : 2,
                    'cannon galleon' : 1,
                    #techs
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :1,

                    #university
                    'masonry'           :1,
                    'architecture'      :0,
                    'stone wall'        :1,
                    'fortified wall'    :0,
                    'guard tower'       :1,
                    'keep'              :0,
                    'bombard tower'     :0,
                    'siege engineers'   :1,     
                    'heated shot'       :1,
                    'treadmill crane'   :1,
                    'arrowslits'        :0,
                    
                    #monastery
                    'redemption'        :0,
                    'atonement'         :0,
                    'herbal medicine'   :1,
                    'heresy'            :1,
                    'sanctity'          :1,
                    'fervor'            :1,
                    'faith'             :0,
                    'illumination'      :1,
                    'block printing'    :1,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :1,
                    'stone 2'           :0,
                    'two man saw'       :1,
                    'guilds'            :0,
                    'crop rotation'     :1,
                    'techslist': None

                },
        
        'malay':
                {
                    
                    #range
                    'archers': 'full',
                    'skirmisher' : 'full',
                    'cavalry archer' : 1,
                    'hand cannon' : 0,
                    #techs
                    'thumb ring'        :1,
                    'parthian tactics'  :0,
                    
                    #barracks
                    'swords' : 4,
                    'spears' : 'full',
                    'eagles' : 0,
                    #techs
                    'arson'             :1, 
                    'squires'           :1, 

                    #stable
                   'light cavalry': 2,
                    'knight' : 2,
                    'camel' : 0,
                    'battle elephant' : 2,
                    #techs
                    'bloodlines'        :0,
                    'husbandry'         :1,
                
                    #workshop
                   'ram' : 2,
                   'mangonel' : 2,
                   'scorpion' : 'full',
                   'bombard cannon' : 1,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :1,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :0,
                    'cavalry armor 3'   :0,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :0,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 'full',
                    'demo ship' : 2,
                    'cannon galleon' : 2,
                    #techs
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :1,

                    #university
                    'masonry'           :1,
                    'architecture'      :0,
                    'stone wall'        :1,
                    'fortified wall'    :0,
                    'guard tower'       :1,
                    'keep'              :1,
                    'bombard tower'     :1,
                    'siege engineers'   :1,     
                    'heated shot'       :1,
                    'treadmill crane'   :0,
                    'arrowslits'        :0,
                    
                    #monastery
                    'redemption'        :1,
                    'atonement'         :1,
                    'herbal medicine'   :1,
                    'heresy'            :1,
                    'sanctity'          :1,
                    'fervor'            :0,
                    'faith'             :1,
                    'illumination'      :1,
                    'block printing'    :1,
                    'theocracy'         :0,
                    #eco techs
                    'gold 2'            :1,
                    'stone 2'           :1,
                    'two man saw'       :0,
                    'guilds'            :1,
                    'crop rotation'     :1,
                    'techslist': None

                }, 
        
        'malians':
                {
                    
                    #range
                    'archers': 'full',
                    'skirmisher' : 'full',
                    'cavalry archer' : 'full',
                    'hand cannon' : 1,
                    #techs
                    'thumb ring'        :1,
                    'parthian tactics'  :0,
                    
                    #barracks
                    'swords' : 'full',
                    'spears' : 2,
                    'eagles' : 0,
                    #techs
                    'arson'             :1, 
                    'squires'           :1, 

                    #stable
                   'light cavalry': 2,
                    'knight' : 2,
                    'camel' : 'full',
                    'battle elephant' : 0,
                    #techs
                    'bloodlines'        :1,
                    'husbandry'         :1,
                
                    #workshop
                   'ram' : 2,
                   'mangonel' : 'full',
                   'scorpion' : 1,
                   'bombard cannon' : 1,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :1,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :0,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :0,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :1,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :0,

                    #dock
                    'galley' : 2,
                    'fire ship' : 'full',
                    'demo ship' : 'full',
                    'cannon galleon' : 1,
                    #techs
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :0,

                    #university
                    'masonry'           :1,
                    'architecture'      :1,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :1,
                    'bombard tower'     :0,
                    'siege engineers'   :0,     
                    'heated shot'       :1,
                    'treadmill crane'   :1,
                    'arrowslits'        :0,
                    
                    #monastery
                    'redemption'        :1,
                    'atonement'         :1,
                    'herbal medicine'   :1,
                    'heresy'            :1,
                    'sanctity'          :1,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :0,
                    'block printing'    :1,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :1,
                    'stone 2'           :1,
                    'two man saw'       :0,
                    'guilds'            :1,
                    'crop rotation'     :1,
                    'techslist': None

                }, 
                
        'mayans':
                {
                    
                    #range
                    'archers': 'full',
                    'skirmisher' : 'full',
                    'cavalry archer' : 0,
                    'hand cannon' : 0,
                    #techs
                    'thumb ring'        :1,
                    'parthian tactics'  :0,
                    
                    #barracks
                    'swords' : 4, #I don't think this is true in HD?
                    'spears' : 'full',
                    'eagles' : 'full',
                    #techs
                    'arson'             :1, 
                    'squires'           :1, 

                    #stable
                   'light cavalry': 0,
                    'knight' : 0,
                    'camel' : 0,
                    'battle elephant' : 0,
                    #techs
                    'bloodlines'        :0,
                    'husbandry'         :0,
                
                    #workshop
                   'ram' : 'full',
                   'mangonel' : 2,
                   'scorpion' : 'full',
                   'bombard cannon' : 0,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :1,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :0,
                    'cavalry armor 2'   :0,
                    'cavalry armor 3'   :0,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :1,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 'full',
                    'demo ship' : 'full',
                    'cannon galleon' : 0,
                    #techs
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :1,

                    #university
                    'masonry'           :1,
                    'architecture'      :1,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :1,
                    'bombard tower'     :0,
                    'siege engineers'   :0,     
                    'heated shot'       :1,
                    'treadmill crane'   :1,
                    'arrowslits'        :0,
                    
                    #monastery
                    'redemption'        :1, #missing in DE but I think this is real
                    'atonement'         :1,
                    'herbal medicine'   :1,
                    'heresy'            :1,
                    'sanctity'          :1,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :0,
                    'block printing'    :1,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :1,
                    'stone 2'           :1,
                    'two man saw'       :0,
                    'guilds'            :1,
                    'crop rotation'     :0,
                    'techslist': None

                }, 
        
        'mongols':
                {
                    
                    #range
                    'archers': 'full',
                    'skirmisher' : 'full',
                    'cavalry archer' : 'full',
                    'hand cannon' : 0,
                    #techs
                    'thumb ring'        :1,
                    'parthian tactics'  :1,
                    
                    #barracks
                    'swords' : 'full',
                    'spears' : 2,
                    'eagles' : 0,
                    #techs
                    'arson'             :1, 
                    'squires'           :1, 

                    #stable
                   'light cavalry': 'full',
                    'knight' : 2,
                    'camel' : 'full',
                    'battle elephant' : 0,
                    #techs
                    'bloodlines'        :1,
                    'husbandry'         :1,
                
                    #workshop
                   'ram' : 'full',
                   'mangonel' : 'full',
                   'scorpion' : 'full',
                   'bombard cannon' : 0,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :0,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :0,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :0,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 'full',
                    'demo ship' : 'full',
                    'cannon galleon' : 1,
                    #techs
                    'careening'         :1,
                    'dry dock'          :0,
                    'shipwright'        :1,

                    #university
                    'masonry'           :1,
                    'architecture'      :0,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :0,
                    'bombard tower'     :0,
                    'siege engineers'   :1,     
                    'heated shot'       :1,
                    'treadmill crane'   :0,
                    'arrowslits'        :0,
                    
                    #monastery
                    'redemption'        :0,
                    'atonement'         :1,
                    'herbal medicine'   :1,
                    'heresy'            :1,
                    'sanctity'          :0,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :0,
                    'block printing'    :0,
                    'theocracy'         :0,
                    #eco techs
                    'gold 2'            :1,
                    'stone 2'           :1,
                    'two man saw'       :0,
                    'guilds'            :0,
                    'crop rotation'     :0,
                    'techslist': None

                }, 

        'persians': #NOTE DONE WITh this YET
                {
                    
                    #range
                    'archers': 2,
                    'skirmisher' : 'full',
                    'cavalry archer' : 'full',
                    'hand cannon' : 1,
                    #techs
                    'thumb ring'        :1,
                    'parthian tactics'  :1,
                    
                    #barracks
                    'swords' : 3,
                    'spears' : 'full',
                    'eagles' : 0,
                    #techs
                    'arson'             :1, 
                    'squires'           :1, 

                    #stable
                   'light cavalry': 'full',
                    'knight' : 'full',
                    'camel' : 'full',
                    'battle elephant' : 0,
                    #techs
                    'bloodlines'        :1,
                    'husbandry'         :1,
                
                    #workshop
                   'ram' : 'full',
                   'mangonel' : 2,
                   'scorpion' : 'full',
                   'bombard cannon' : 1,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :1,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :0,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :1,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :0,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 'full',
                    'demo ship' : 'full',
                    'cannon galleon' : 'full',
                    #techs
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :0,

                    #university
                    'masonry'           :1,
                    'architecture'      :1,
                    'stone wall'        :1,
                    'fortified wall'    :0,
                    'guard tower'       :1,
                    'keep'              :0,
                    'bombard tower'     :0,
                    'siege engineers'   :0,     
                    'heated shot'       :1,
                    'treadmill crane'   :0,
                    'arrowslits'        :0,
                    
                    #monastery
                    'redemption'        :0,
                    'atonement'         :0,
                    'herbal medicine'   :1,
                    'heresy'            :0,
                    'sanctity'          :0,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :0,
                    'block printing'    :1,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :1,
                    'stone 2'           :1,
                    'two man saw'       :1,
                    'guilds'            :1,
                    'crop rotation'     :1,
                    'techslist': None

                }, 
        
        'portuguese':
                {
                    
                    #range
                    'archers': 'full',
                    'skirmisher' : 'full',
                    'cavalry archer' : 1,
                    'hand cannon' : 1,
                    #techs
                    'thumb ring'        :1,
                    'parthian tactics'  :0,
                    
                    #barracks
                    'swords' : 'full',
                    'spears' : 'full',
                    'eagles' : 0,
                    #techs
                    'arson'             :1, 
                    'squires'           :0, 

                    #stable
                   'light cavalry': 2,
                    'knight' : 2,
                    'camel' : 0,
                    'battle elephant' : 0,
                    #techs
                    'bloodlines'        :1,
                    'husbandry'         :1,
                
                    #workshop
                   'ram' : 2,
                   'mangonel' : 2,
                   'scorpion' : 1,
                   'bombard cannon' : 1,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :1,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :1,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :1,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 2,
                    'demo ship' : 'full',
                    'cannon galleon' : 2,
                    #techs
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :0,

                    #university
                    'masonry'           :1,
                    'architecture'      :1,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :1,
                    'bombard tower'     :1,
                    'siege engineers'   :1,     
                    'heated shot'       :1,
                    'treadmill crane'   :1,
                    'arrowslits'        :0,
                    
                    #monastery
                    'redemption'        :1,
                    'atonement'         :1,
                    'herbal medicine'   :1,
                    'heresy'            :1,
                    'sanctity'          :1,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :0,
                    'block printing'    :1,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :0,
                    'stone 2'           :1,
                    'two man saw'       :1,
                    'guilds'            :1,
                    'crop rotation'     :1,
                    'techslist': None

                }, 
        
        'saracens':
                {
                    
                    #range
                    'archers': 'full',
                    'skirmisher' : 'full',
                    'cavalry archer' : 'full',
                    'hand cannon' : 1,
                    #techs
                    'thumb ring'        :1,
                    'parthian tactics'  :1,
                    
                    #barracks
                    'swords' : 'full',
                    'spears' : 2,
                    'eagles' : 0,
                    #techs
                    'arson'             :1, 
                    'squires'           :1, 

                    #stable
                   'light cavalry': 'full',
                    'knight' : 1,
                    'camel' : 'full',
                    'battle elephant' : 0,
                    #techs
                    'bloodlines'        :1,
                    'husbandry'         :1,
                
                    #workshop
                   'ram' : 'full',
                   'mangonel' : 'full',
                   'scorpion' : 1,
                   'bombard cannon' : 1,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :1,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :1,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :1,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 2,
                    'demo ship' : 'full',
                    'cannon galleon' : 2,
                    #techs
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :0,

                    #university
                    'masonry'           :1,
                    'architecture'      :0,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :1,
                    'bombard tower'     :0,
                    'siege engineers'   :1,     
                    'heated shot'       :0,
                    'treadmill crane'   :1,
                    'arrowslits'        :1,
                    
                    #monastery
                    'redemption'        :1,
                    'atonement'         :1,
                    'herbal medicine'   :1,
                    'heresy'            :1,
                    'sanctity'          :1,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :1,
                    'block printing'    :1,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :1,
                    'stone 2'           :0,
                    'two man saw'       :1,
                    'guilds'            :0,
                    'crop rotation'     :0,
                    'techslist': None

                }, 
        
        'slavs':
                {
                    
                    #range
                    'archers': 2,
                    'skirmisher' : 'full',
                    'cavalry archer' : 'full',
                    'hand cannon' : 0,
                    #techs
                    'thumb ring'        :0,
                    'parthian tactics'  :0,
                    
                    #barracks
                    'swords' : 'full',
                    'spears' : 'full',
                    'eagles' : 0,
                    #techs
                    'arson'             :1, 
                    'squires'           :1, 

                    #stable
                   'light cavalry': 'full',
                    'knight' : 2,
                    'camel' : 0,
                    'battle elephant' : 0,
                    #techs
                    'bloodlines'        :1,
                    'husbandry'         :1,
                
                    #workshop
                   'ram' : 'full',
                   'mangonel' : 'full',
                   'scorpion' : 'full',
                   'bombard cannon' : 0,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :0,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :1,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :0,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 'full',
                    'demo ship' : 2,
                    'cannon galleon' : 1,
                    #techs
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :0,

                    #university
                    'masonry'           :1,
                    'architecture'      :0,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :0,
                    'bombard tower'     :0,
                    'siege engineers'   :1,     
                    'heated shot'       :0,
                    'treadmill crane'   :1,
                    'arrowslits'        :0,
                    
                    #monastery
                    'redemption'        :1,
                    'atonement'         :1,
                    'herbal medicine'   :1,
                    'heresy'            :0,
                    'sanctity'          :1,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :1,
                    'block printing'    :1,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :1,
                    'stone 2'           :0,
                    'two man saw'       :1,
                    'guilds'            :0,
                    'crop rotation'     :1,
                    'techslist': None

                }, 
        
        'spanish':
                {
                    
                    #range
                    'archers': 1,
                    'skirmisher' : 'full',
                    'cavalry archer' : 'full',
                    'hand cannon' : 1,
                    #techs
                    'thumb ring'        :1,
                    'parthian tactics'  :0,
                    
                    #barracks
                    'swords' : 'full',
                    'spears' : 'full',
                    'eagles' : 0,
                    #techs
                    'arson'             :1, 
                    'squires'           :1, 

                    #stable
                   'light cavalry': 'full',
                    'knight' : 'full',
                    'camel' : 0,
                    'battle elephant' : 0,
                    #techs
                    'bloodlines'        :1,
                    'husbandry'         :1,
                
                    #workshop
                   'ram' : 'full',
                   'mangonel' : 2,
                   'scorpion' : 1,
                   'bombard cannon' : 1,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :1,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :1,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :1,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 'full',
                    'demo ship' : 'full',
                    'cannon galleon' : 'full',
                    #techs
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :1,

                    #university
                    'masonry'           :1,
                    'architecture'      :1,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :1,
                    'bombard tower'     :1,
                    'siege engineers'   :0,     
                    'heated shot'       :0,
                    'treadmill crane'   :0,
                    'arrowslits'        :1,
                    
                    #monastery
                    'redemption'        :1,
                    'atonement'         :1,
                    'herbal medicine'   :1,
                    'heresy'            :1,
                    'sanctity'          :1,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :1,
                    'block printing'    :1,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :0,
                    'stone 2'           :1,
                    'two man saw'       :1,
                    'guilds'            :1,
                    'crop rotation'     :0,
                    'techslist': None

                }, 
        
        'teutons':
                {
                    
                    #range
                    'archers': 2,
                    'skirmisher' : 'full',
                    'cavalry archer' : 1,
                    'hand cannon' : 1,
                    #techs
                    'thumb ring'        :0,
                    'parthian tactics'  :0,
                    
                    #barracks
                    'swords' : 'full',
                    'spears' : 'full',
                    'eagles' : 0,
                    #techs
                    'arson'             :1, 
                    'squires'           :1, 

                    #stable
                   'light cavalry': 1,
                    'knight' : 'full',
                    'camel' : 0,
                    'battle elephant' : 0,
                    #techs
                    'bloodlines'        :1,
                    'husbandry'         :0,
                
                    #workshop
                   'ram' : 2,
                   'mangonel' : 'full',
                   'scorpion' : 'full',
                   'bombard cannon' : 1,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :1,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :0,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :1,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :0,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 'full',
                    'demo ship' : 'full',
                    'cannon galleon' : 1,
                    #techs
                    'careening'         :1,
                    'dry dock'          :0,
                    'shipwright'        :0,

                    #university
                    'masonry'           :1,
                    'architecture'      :0,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :1,
                    'bombard tower'     :1,
                    'siege engineers'   :1,     
                    'heated shot'       :1,
                    'treadmill crane'   :1,
                    'arrowslits'        :1,
                    
                    #monastery
                    'redemption'        :1,
                    'atonement'         :1,
                    'herbal medicine'   :1,
                    'heresy'            :1,
                    'sanctity'          :1,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :1,
                    'block printing'    :1,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :0,
                    'stone 2'           :1,
                    'two man saw'       :1,
                    'guilds'            :1,
                    'crop rotation'     :1,
                    'techslist': None

                }, 
        
        'turks':
                {
                    
                    #range
                    'archers': 2,
                    'skirmisher' : 1,
                    'cavalry archer' : 'full',
                    'hand cannon' : 1,
                    #techs
                    'thumb ring'        :1,
                    'parthian tactics'  :1,
                    
                    #barracks
                    'swords' : 'full',
                    'spears' : 1,
                    'eagles' : 0,
                    #techs
                    'arson'             :1, 
                    'squires'           :1, 

                    #stable
                   'light cavalry': 'full',
                    'knight' : 2,
                    'camel' : 'full',
                    'battle elephant' : 0,
                    #techs
                    'bloodlines'        :1,
                    'husbandry'         :1,
                
                    #workshop
                   'ram' : 'full',
                   'mangonel' : 1,
                   'scorpion' : 'full',
                   'bombard cannon' : 1,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :1,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :1,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :1,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 2,
                    'demo ship' : 'full',
                    'cannon galleon' : 2,
                    #techs
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :1,

                    #university
                    'masonry'           :1,
                    'architecture'      :1,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :1,
                    'bombard tower'     :1,
                    'siege engineers'   :0,     
                    'heated shot'       :1,
                    'treadmill crane'   :1,
                    'arrowslits'        :1,
                    
                    #monastery
                    'redemption'        :1,
                    'atonement'         :1,
                    'herbal medicine'   :0,
                    'heresy'            :1,
                    'sanctity'          :1,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :0,
                    'block printing'    :0,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :1,
                    'stone 2'           :0,
                    'two man saw'       :1,
                    'guilds'            :1,
                    'crop rotation'     :0,
                    'techslist': None

                }, 
        
        'vietnamese':
                {
                    
                    #range
                    'archers': 'full',
                    'skirmisher' : 'full',
                    'cavalry archer' : 'full',
                    'hand cannon' : 0,
                    #techs
                    'thumb ring'        :1,
                    'parthian tactics'  :0,
                    
                    #barracks
                    'swords' : 'full',
                    'spears' : 'full',
                    'eagles' : 0,
                    #techs
                    'arson'             :1, 
                    'squires'           :1, 

                    #stable
                   'light cavalry': 2,
                    'knight' : 2,
                    'camel' : 0,
                    'battle elephant' : 'full',
                    #techs
                    'bloodlines'        :1,
                    'husbandry'         :1,
                
                    #workshop
                   'ram' : 2,
                   'mangonel' : 2,
                   'scorpion' : 1,
                   'bombard cannon' : 1,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :1,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :0,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :1,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :0,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 2,
                    'demo ship' : 'full',
                    'cannon galleon' : 'full',
                    #techs
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :0,

                    #university
                    'masonry'           :0,
                    'architecture'      :0,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :1,
                    'bombard tower'     :1,
                    'siege engineers'   :1,     
                    'heated shot'       :1,
                    'treadmill crane'   :1,
                    'arrowslits'        :1,
                    
                    #monastery
                    'redemption'        :0,
                    'atonement'         :1,
                    'herbal medicine'   :1,
                    'heresy'            :0,
                    'sanctity'          :1,
                    'fervor'            :0,
                    'faith'             :1,
                    'illumination'      :1,
                    'block printing'    :1,
                    'theocracy'         :1,
                    #eco techs
                    'gold 2'            :0,
                    'stone 2'           :1,
                    'two man saw'       :1,
                    'guilds'            :1,
                    'crop rotation'     :1,
                    'techslist': None

                }, 
        
        'vikings':
                {
                    
                    #range
                    'archers': 'full',
                    'skirmisher' : 'full',
                    'cavalry archer' : 1,
                    'hand cannon' : 0,
                    #techs
                    'thumb ring'        :1,
                    'parthian tactics'  :0,
                    
                    #barracks
                    'swords' : 'full',
                    'spears' : 2,
                    'eagles' : 0,
                    #techs
                    'arson'             :1, 
                    'squires'           :1, 

                    #stable
                   'light cavalry': 2,
                    'knight' : 2,
                    'camel' : 0,
                    'battle elephant' : 0,
                    #techs
                    'bloodlines'        :0,
                    'husbandry'         :0,
                
                    #workshop
                   'ram' : 'full',
                   'mangonel' : 2,
                   'scorpion' : 'full',
                   'bombard cannon' : 0,
                    
                    
                    #blacksmith
                    'archer armor 1'    :1,
                    'archer armor 2'    :1,
                    'archer armor 3'    :1,
                    'fletching'         :1,
                    'bodkin arrow'      :1,
                    'bracer'            :1,
                    'melee attack 1'    :1,
                    'melee attack 2'    :1,
                    'melee attack 3'    :1,
                    'cavalry armor 1'   :1,
                    'cavalry armor 2'   :1,
                    'cavalry armor 3'   :0,
                    'infantry armor 1'  :1,
                    'infantry armor 2'  :1,
                    'infantry armor 3'  :1,
                'full blacksmith'       :0,

                    #dock
                    'galley' : 'full',
                    'fire ship' : 0,
                    'demo ship' : 'full',
                    'cannon galleon' : 'full',
                    #techs
                    'careening'         :1,
                    'dry dock'          :1,
                    'shipwright'        :0,

                    #university
                    'masonry'           :1,
                    'architecture'      :1,
                    'stone wall'        :1,
                    'fortified wall'    :1,
                    'guard tower'       :1,
                    'keep'              :0,
                    'bombard tower'     :0,
                    'siege engineers'   :1,     
                    'heated shot'       :1,
                    'treadmill crane'   :1,
                    'arrowslits'        :1,
                    
                    #monastery
                    'redemption'        :0,
                    'atonement'         :1,
                    'herbal medicine'   :0,
                    'heresy'            :1,
                    'sanctity'          :0,
                    'fervor'            :1,
                    'faith'             :1,
                    'illumination'      :0,
                    'block printing'    :1,
                    'theocracy'         :0,
                    #eco techs
                    'gold 2'            :1,
                    'stone 2'           :0,
                    'two man saw'       :1,
                    'guilds'            :0,
                    'crop rotation'     :1,
                    'techslist': None

                }        
        
            }
    return attributes

def make_civ_dict(unitlist, civ_info):
    civ_unitlist = {}
    for bkey in unitlist.keys():
        for unitline in unitlist[bkey]:
            if civ_info[unitline] == 'full':
                for unit in unitlist[bkey][unitline]:
                    civ_unitlist[unit] = 1;
            elif type(civ_info[unitline]) == int:
                i = 0
                for unit in unitlist[bkey][unitline]:
                    civ_unitlist[unit] = 1 if i < civ_info[unitline] else 0
                    i += 1
            #the non-sequential tech case
            else: 
                for tech in unitlist[bkey][unitline]:
                    civ_unitlist[tech] = 1 if civ_info[tech] == 1 else 0
                
    return civ_unitlist
