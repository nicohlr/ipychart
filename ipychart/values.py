KINDS = ['line', 'bar', 'radar', 'doughnut', 'polarArea', 'bubble',
         'pie', 'scatter']

COLORSCHEMES = [
    'brewer.YlGn3', 'brewer.YlGn4', 'brewer.YlGn5', 'brewer.YlGn6',
    'brewer.YlGn7', 'brewer.YlGn8', 'brewer.YlGn9', 'brewer.YlGnBu3',
    'brewer.YlGnBu4', 'brewer.YlGnBu5', 'brewer.YlGnBu6', 'brewer.YlGnBu7',
    'brewer.YlGnBu8', 'brewer.YlGnBu9', 'brewer.GnBu3', 'brewer.GnBu4',
    'brewer.GnBu5', 'brewer.GnBu6', 'brewer.GnBu7', 'brewer.GnBu8',
    'brewer.GnBu9', 'brewer.BuGn3', 'brewer.BuGn4', 'brewer.BuGn5',
    'brewer.BuGn6', 'brewer.BuGn7', 'brewer.BuGn8', 'brewer.BuGn9',
    'brewer.PuBuGn3', 'brewer.PuBuGn4', 'brewer.PuBuGn5', 'brewer.PuBuGn6',
    'brewer.PuBuGn7', 'brewer.PuBuGn8', 'brewer.PuBuGn9', 'brewer.PuBu3',
    'brewer.PuBu4', 'brewer.PuBu5', 'brewer.PuBu6', 'brewer.PuBu7',
    'brewer.PuBu8', 'brewer.PuBu9', 'brewer.BuPu3', 'brewer.BuPu4',
    'brewer.BuPu5', 'brewer.BuPu6', 'brewer.BuPu7', 'brewer.BuPu8',
    'brewer.BuPu9', 'brewer.RdPu3', 'brewer.RdPu4', 'brewer.RdPu5',
    'brewer.RdPu6', 'brewer.RdPu7', 'brewer.RdPu8', 'brewer.RdPu9',
    'brewer.PuRd3', 'brewer.PuRd4', 'brewer.PuRd5', 'brewer.PuRd6',
    'brewer.PuRd7', 'brewer.PuRd8', 'brewer.PuRd9', 'brewer.OrRd3',
    'brewer.OrRd4', 'brewer.OrRd5', 'brewer.OrRd6', 'brewer.OrRd7',
    'brewer.OrRd8', 'brewer.OrRd9', 'brewer.YlOrRd3', 'brewer.YlOrRd4',
    'brewer.YlOrRd5', 'brewer.YlOrRd6', 'brewer.YlOrRd7', 'brewer.YlOrRd8',
    'brewer.YlOrRd9', 'brewer.YlOrBr3', 'brewer.YlOrBr4', 'brewer.YlOrBr5',
    'brewer.YlOrBr6', 'brewer.YlOrBr7', 'brewer.YlOrBr8', 'brewer.YlOrBr9',
    'brewer.Purples3', 'brewer.Purples4', 'brewer.Purples5', 'brewer.Purples6',
    'brewer.Purples7', 'brewer.Purples8', 'brewer.Purples9', 'brewer.Blues3',
    'brewer.Blues4', 'brewer.Blues5', 'brewer.Blues6', 'brewer.Blues7',
    'brewer.Blues8', 'brewer.Blues9', 'brewer.Greens3', 'brewer.Greens4',
    'brewer.Greens5', 'brewer.Greens6', 'brewer.Greens7', 'brewer.Greens8',
    'brewer.Greens9', 'brewer.Oranges3', 'brewer.Oranges4', 'brewer.Oranges5',
    'brewer.Oranges6', 'brewer.Oranges7', 'brewer.Oranges8', 'brewer.Oranges9',
    'brewer.Reds3', 'brewer.Reds4', 'brewer.Reds5', 'brewer.Reds6',
    'brewer.Reds7', 'brewer.Reds8', 'brewer.Reds9', 'brewer.Greys3',
    'brewer.Greys4', 'brewer.Greys5', 'brewer.Greys6', 'brewer.Greys7',
    'brewer.Greys8', 'brewer.Greys9', 'brewer.PuOr3', 'brewer.PuOr4',
    'brewer.PuOr5', 'brewer.PuOr6', 'brewer.PuOr7', 'brewer.PuOr8',
    'brewer.PuOr9', 'brewer.PuOr10', 'brewer.PuOr11', 'brewer.BrBG3',
    'brewer.BrBG4', 'brewer.BrBG5', 'brewer.BrBG6', 'brewer.BrBG7',
    'brewer.BrBG8', 'brewer.BrBG9', 'brewer.BrBG10', 'brewer.BrBG11',
    'brewer.PRGn3', 'brewer.PRGn4', 'brewer.PRGn5', 'brewer.PRGn6',
    'brewer.PRGn7', 'brewer.PRGn8', 'brewer.PRGn9', 'brewer.PRGn10',
    'brewer.PRGn11', 'brewer.PiYG3', 'brewer.PiYG4', 'brewer.PiYG5',
    'brewer.PiYG6', 'brewer.PiYG7', 'brewer.PiYG8', 'brewer.PiYG9',
    'brewer.PiYG10', 'brewer.PiYG11', 'brewer.RdBu3', 'brewer.RdBu4',
    'brewer.RdBu5', 'brewer.RdBu6', 'brewer.RdBu7', 'brewer.RdBu8',
    'brewer.RdBu9', 'brewer.RdBu10', 'brewer.RdBu11', 'brewer.RdGy3',
    'brewer.RdGy4', 'brewer.RdGy5', 'brewer.RdGy6', 'brewer.RdGy7',
    'brewer.RdGy8', 'brewer.RdGy9', 'brewer.RdGy10', 'brewer.RdGy11',
    'brewer.RdYlBu3', 'brewer.RdYlBu4', 'brewer.RdYlBu5', 'brewer.RdYlBu6',
    'brewer.RdYlBu7', 'brewer.RdYlBu8', 'brewer.RdYlBu9', 'brewer.RdYlBu10',
    'brewer.RdYlBu11', 'brewer.Spectral3', 'brewer.Spectral4',
    'brewer.Spectral5', 'brewer.Spectral6', 'brewer.Spectral7',
    'brewer.Spectral8', 'brewer.Spectral9', 'brewer.Spectral10',
    'brewer.Spectral11', 'brewer.RdYlGn3', 'brewer.RdYlGn4', 'brewer.RdYlGn5',
    'brewer.RdYlGn6', 'brewer.RdYlGn7', 'brewer.RdYlGn8', 'brewer.RdYlGn9',
    'brewer.RdYlGn10', 'brewer.RdYlGn11', 'brewer.Accent3', 'brewer.Accent4',
    'brewer.Accent5', 'brewer.Accent6', 'brewer.Accent7', 'brewer.Accent8',
    'brewer.DarkTwo3', 'brewer.DarkTwo4', 'brewer.DarkTwo5', 'brewer.DarkTwo6',
    'brewer.DarkTwo7', 'brewer.DarkTwo8', 'brewer.Paired3', 'brewer.Paired4',
    'brewer.Paired5', 'brewer.Paired6', 'brewer.Paired7', 'brewer.Paired8',
    'brewer.Paired9', 'brewer.Paired10', 'brewer.Paired11', 'brewer.Paired12',
    'brewer.PastelOne3', 'brewer.PastelOne4', 'brewer.PastelOne5',
    'brewer.PastelOne6', 'brewer.PastelOne7', 'brewer.PastelOne8',
    'brewer.PastelOne9', 'brewer.PastelTwo3', 'brewer.PastelTwo4',
    'brewer.PastelTwo5', 'brewer.PastelTwo6', 'brewer.PastelTwo7',
    'brewer.PastelTwo8', 'brewer.SetOne3', 'brewer.SetOne4', 'brewer.SetOne5',
    'brewer.SetOne6', 'brewer.SetOne7', 'brewer.SetOne8', 'brewer.SetOne9',
    'brewer.SetTwo3', 'brewer.SetTwo4', 'brewer.SetTwo5', 'brewer.SetTwo6',
    'brewer.SetTwo7', 'brewer.SetTwo8', 'brewer.SetThree3', 'brewer.SetThree4',
    'brewer.SetThree5', 'brewer.SetThree6', 'brewer.SetThree7',
    'brewer.SetThree8', 'brewer.SetThree9', 'brewer.SetThree10',
    'brewer.SetThree11', 'brewer.SetThree12', 'office.Adjacency6',
    'office.Advantage6', 'office.Angles6', 'office.Apex6',
    'office.Apothecary6', 'office.Aspect6', 'office.Atlas6', 'office.Austin6',
    'office.Badge6', 'office.Banded6', 'office.Basis6', 'office.Berlin6',
    'office.BlackTie6', 'office.Blue6', 'office.BlueGreen6', 'office.BlueII6',
    'office.BlueRed6', 'office.BlueWarm6', 'office.Breeze6', 'office.Capital6',
    'office.Celestial6', 'office.Circuit6', 'office.Civic6', 'office.Clarity6',
    'office.Codex6', 'office.Composite6', 'office.Concourse6',
    'office.Couture6', 'office.Crop6', 'office.Damask6', 'office.Depth6',
    'office.Dividend6', 'office.Droplet6', 'office.Elemental6',
    'office.Equity6', 'office.Essential6', 'office.Excel16',
    'office.Executive6', 'office.Exhibit6', 'office.Expo6', 'office.Facet6',
    'office.Feathered6', 'office.Flow6', 'office.Focus6', 'office.Folio6',
    'office.Formal6', 'office.Forte6', 'office.Foundry6', 'office.Frame6',
    'office.Gallery6', 'office.Genesis6', 'office.Grayscale6', 'office.Green6',
    'office.GreenYellow6', 'office.Grid6', 'office.Habitat6',
    'office.Hardcover6', 'office.Headlines6', 'office.Horizon6',
    'office.Infusion6', 'office.Inkwell6', 'office.Inspiration6',
    'office.Integral6', 'office.Ion6', 'office.IonBoardroom6',
    'office.Kilter6', 'office.Madison6', 'office.MainEvent6',
    'office.Marquee6', 'office.Median6', 'office.Mesh6', 'office.Metail6',
    'office.Metro6', 'office.Metropolitan6', 'office.Module6',
    'office.NewsPrint6', 'office.Office6', 'office.OfficeClassic6',
    'office.Opulent6', 'office.Orange6', 'office.OrangeRed6', 'office.Orbit6',
    'office.Organic6', 'office.Oriel6', 'office.Origin6', 'office.Paper6',
    'office.Parallax6', 'office.Parcel6', 'office.Perception6',
    'office.Perspective6', 'office.Pixel6', 'office.Plaza6',
    'office.Precedent6', 'office.Pushpin6', 'office.Quotable6', 'office.Red6',
    'office.RedOrange6', 'office.RedViolet6', 'office.Retrospect6',
    'office.Revolution6', 'office.Saddle6', 'office.Savon6',
    'office.Sketchbook6', 'office.Sky6', 'office.Slate6', 'office.Slice6',
    'office.Slipstream6', 'office.SOHO6', 'office.Solstice6',
    'office.Spectrum6', 'office.Story6', 'office.Studio6', 'office.Summer6',
    'office.Technic6', 'office.Thatch6', 'office.Tradition6',
    'office.Travelogue6', 'office.Trek6', 'office.Twilight6', 'office.Urban6',
    'office.UrbanPop6', 'office.VaporTrail6', 'office.Venture6',
    'office.Verve6', 'office.View6', 'office.Violet6', 'office.VioletII6',
    'office.Waveform6', 'office.Wisp6', 'office.WoodType6', 'office.Yellow6',
    'office.YellowOrange6', 'tableau.Tableau10', 'tableau.Tableau20',
    'tableau.ColorBlind10', 'tableau.SeattleGrays5', 'tableau.Traffic9',
    'tableau.MillerStone11', 'tableau.SuperfishelStone10',
    'tableau.NurielStone9', 'tableau.JewelBright9', 'tableau.Summer8',
    'tableau.Winter10', 'tableau.GreenOrangeTeal12', 'tableau.RedBlueBrown12',
    'tableau.PurplePinkGray12', 'tableau.HueCircle19', 'tableau.OrangeBlue7',
    'tableau.RedGreen7', 'tableau.GreenBlue7', 'tableau.RedBlue7',
    'tableau.RedBlack7', 'tableau.GoldPurple7', 'tableau.RedGreenGold7',
    'tableau.SunsetSunrise7', 'tableau.OrangeBlueWhite7',
    'tableau.RedGreenWhite7', 'tableau.GreenBlueWhite7',
    'tableau.RedBlueWhite7', 'tableau.RedBlackWhite7',
    'tableau.OrangeBlueLight7', 'tableau.Temperature7', 'tableau.BlueGreen7',
    'tableau.BlueLight7', 'tableau.OrangeLight7', 'tableau.Blue20',
    'tableau.Orange20', 'tableau.Green20', 'tableau.Red20', 'tableau.Purple20',
    'tableau.Brown20', 'tableau.Gray20', 'tableau.GrayWarm20',
    'tableau.BlueTeal20', 'tableau.OrangeGold20', 'tableau.GreenGold20',
    'tableau.RedGold21', 'tableau.Classic10', 'tableau.ClassicMedium10',
    'tableau.ClassicLight10', 'tableau.Classic20', 'tableau.ClassicGray5',
    'tableau.ClassicColorBlind10', 'tableau.ClassicTrafficLight9',
    'tableau.ClassicPurpleGray6', 'tableau.ClassicPurpleGray12',
    'tableau.ClassicGreenOrange6', 'tableau.ClassicGreenOrange12',
    'tableau.ClassicBlueRed6', 'tableau.ClassicBlueRed12',
    'tableau.ClassicCyclic13', 'tableau.ClassicGreen7',
    'tableau.ClassicGray13', 'tableau.ClassicBlue7', 'tableau.ClassicRed9',
    'tableau.ClassicOrange7', 'tableau.ClassicAreaRed11',
    'tableau.ClassicAreaGreen11', 'tableau.ClassicAreaBrown11',
    'tableau.ClassicRedGreen11', 'tableau.ClassicRedBlue11',
    'tableau.ClassicRedBlack11', 'tableau.ClassicAreaRedGreen21',
    'tableau.ClassicOrangeBlue13', 'tableau.ClassicGreenBlue11',
    'tableau.ClassicRedWhiteGreen11', 'tableau.ClassicRedWhiteBlack11',
    'tableau.ClassicOrangeWhiteBlue11', 'tableau.ClassicRedWhiteBlackLight10',
    'tableau.ClassicOrangeWhiteBlueLight11',
    'tableau.ClassicRedWhiteGreenLight11', 'tableau.ClassicRedGreenLight11'
]
