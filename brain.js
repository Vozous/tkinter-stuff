window.onload = function(){

    const ImageList = {
        //water: "https://www.publicdomainpictures.net/pictures/30000/velka/plain-white-background.jpg",
        hit: "https://www.flaticon.com/svg/static/icons/svg/616/616500.svg",
        water: "https://cdn.iconscout.com/icon/free/png-256/ocean-water-wave-sea-tsunami-38119.png",
        missed: "https://d1nhio0ox7pgb.cloudfront.net/_img/o_collection_png/green_dark_grey/512x512/plain/navigate_cross.png",
        boat1: "https://i.imgur.com/JfwAhJc.png",
        boat2: "https://i.imgur.com/En6WFg8.png",
        boat3: "https://i.imgur.com/MGLxQRg.png"
    }
    
    const CheckPlaces = [
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1]
    ]

    const ShipList = {
            aircraft: {
                name: "Porte Avion",
                length: 5,
                images: []
            },
            cruiser: {
                name: "Croiseur",
                length: 4,
                images: []
            },
            countertorpedo: {
                name: "Contre Torpilleur",
                length: 3,
                images: []
            },
            torpedo: {
                name: "Torpilleur",
                length: 3,
                images: []
            },
            submarine: {
                name: "Sous-Marin",
                length: 2,
                images: []
            }
    }

    var Ship = class{
        constructor(map, name, length, images, td, computer){
            this.map = map
            this.name = name
            this.image = images
            this.length = length
            this.computer = computer;
            this.placed = false
            this.alive = true;
            this.td = td
            this.blocks = []
        }

        place(x, y, x2, y2, dir){
            this.map.tracepos(x, y, x2, y2, (hitblock, final, start)=>{
                this.blocks.push(hitblock);
                hitblock.ship    = this
                hitblock.name    = this.name;
                hitblock.hit     = false;

                let game = this.map.game;
                let ship = this;

                if(!this.computer){
                    hitblock.image   = start  ? ImageList["boat1"] : final ? ImageList["boat3"] : ImageList["boat2"];
                    Rotate(hitblock.td, this.getrotation(dir));
                }

                hitblock.left    = function(){

                    if(game.started){
                        if((game.playerturn && ship.computer) || (!game.playerturn && !ship.computer)){
                            hitblock.hit = true;
                            hitblock.image = ImageList["hit"];
                            ship.checkstate();
                        }
                    }else{
                        if(!ship.map.selectedship){
                            ship.blocks.forEach((block)=>{
                                hitblock.ship = undefined;
                                let newblock = Block_Water(block)
                                ship.map.setpos(block.x, block.y, newblock);
                                Rotate(newblock.td, 0);
                            })

                            ship.blocks = [];

                            ship.placed = false;
                        }
                    }
                }
            })

            this.placed = true;
        }

        checkstate(){
            let alive = false;

            this.blocks.forEach((block)=>{
                if(!block.hit){
                    alive = true;
                }
            })

            if(!alive){
                this.alive = false;

                this.map.game.checkwin();
            }
        }

        getrotation(dir){
            let x = dir[0];
            let y = dir[1];

            return ((1-0.5*(y+1))*180)*Math.abs(y)+((1-0.5*(x+1))*180+90)*Math.abs(x)
        }

        click(){
            if(this.map.game.started){

            }else{
                if((!this.placed) && this.map.selectedblocks.length == 0){
                    if(this.map.selectedship && this.map.selectedship == this){
                        this.map.selectedship = undefined
                    }else{
                       this.map.selectedship = this
                    }
                }
            }
        }
    }

    var Block = class{

        set selected(bool){
            Activate(this.td, bool, "lime")
            this._selected = bool
        }

        set image(img){
            img = img ? img : this._image

            this.td.style["background"] =  "url(" + img + ") no-repeat"
            this.td.style["background-size"] =  "100%"

            this._image = img
        }

        set name(str){
            let img = ImageList[str]
            if(img){
                this.image  = img;
            }
            this._name      = str
            this.left       = undefined
            this.clickeable = undefined
        }

        get image(){
            return this._image
        }

        get name(){
            return this._name
        }

        get selected(){
            return this._selected
        }

        constructor(map, td, x, y, name, left, canclick){
            this.map = map
            this.td = td
            this.x = x
            this.y = y
            this.name = name
            this.left  = left
            this.canclick = canclick;
            this._selected = false
        }

        click(computer){
            if(this.left){
                this.left(computer)
            }
        }
    }

    var Block_Water = function(block){

        if(!block){
            block = Block(map, td, x, y)
        }else{
            block.name = "water";
        }

        block.left = (computer)=>{
            let map = block.map;

            if(map.game.started){
                if(map.game.playerturn){
                    if(computer){
                        block.name = "missed";
                        map.game.switchTurn();
                    }
                }else{
                    if(!computer){
                        block.name = "missed";
                        map.game.switchTurn();
                    }
                }
            }else{
                if(map.selected){
                    if(map.selected == block){
                        map.selected = undefined
                        map.unselectall()
                    }else{
                        if(block.td.style["border-color"] == "orange"){
                            let dir = map.dirvector(map.selected.x, map.selected.y, block.x, block.y)
                            
                            let x_vec = map.selected.x + dir[0] * (map.selectedship.length - 1)
                            let y_vec = map.selected.y + dir[1] * (map.selectedship.length - 1)

                            map.selectedship.place(map.selected.x, map.selected.y, x_vec, y_vec, dir)
                            
                            map.selected     = undefined
                            map.selectedship = undefined

                            map.unselectall()

                            map.checkroundstarto()
                        }
                    }
                }else{
                    if(map.selectedship){
                        let possibilities = map.traceship(block.x, block.y, map.selectedship.length);
                        if(possibilities){
                            map.showpath(block.x, block.y, possibilities);
                            map.selected = block
                        }else{
                            Activate(block.td, true, "red");
                            setTimeout(()=>{
                                if(block.td.style["border-color"] = "red"){
                                    Activate(block.td, false);
                                }                                    
                            }, 1000);
                        }
                    }
                }
            }
        }

        return block
    }
    
    var Activate = function(element, bool, clr){
        if(bool){
            element.style["border"] = "solid 2px " + clr;
        }else{
            element.style["border"] = ""
        }
    }

    var Rotate = function(element, deg){
        element.style["transform"] = "rotate(" + deg + "deg)";
    }

    var Map = class{

        constructor(game, html_body, html_ships, name, w, h, computer){
            this.game = game
            this.name = name
            this.width = w
            this.height = h
            this._selected = undefined
            this._selectedship = undefined
            this.ships = []

            this.selectedblocks = []

            let map = this

            html_body.innerHTML = ""

            for (let x=1; x<map.width+1; x++){
                let tr = document.createElement("tr")
                html_body.appendChild(tr);
                map[x] = []
                for (let y=1; y<map.height+1; y++){
                    let td = document.createElement("td")
                    let block = new Block(map, td, x, y)
                    Block_Water(block);

                    tr.classList.add("tables__row");
                    td.classList.add("tables__item");

                    map[x][y] = block

                    td.onclick = function(){
                        if((!map.game.started) || (map.game.playerturn)){
                            block.click(computer)
                        }
                    }

                    tr.appendChild(td);
                }
            }

            for (let k in ShipList){
                
                let data = ShipList[k];

                let div = document.createElement("div")
                div.classList.add("asides__item");
                html_ships.appendChild(div);
                div.innerHTML = data.name
                
                let ship = new Ship(map, data.name, data.length, data.images, div, computer)

                map.ships.push(ship)

                if(!computer){
                    div.onclick = function(){
                        ship.click()
                    }
                }
            }
        }

        checkroundstarto(){
            let starto = true

            this.ships.forEach((ship)=>{
                if(!ship.placed){
                    starto = false
                    return
                }
            })

            if(starto){
                this.game.started = true;
            }
        }

        unselectall(){
            this.selectedblocks.forEach((block)=>{
                Activate(block.td, false)
            })

            this.selectedblocks = [];
        }

        setpos(x, y, block){
            if(this[x] && this[x][y]){
                this[x][y] = block;
                return block;
            }
        }

        getpos(x, y){
            if(this[x] && this[x][y]){
                return this[x][y]
            }
        }

        distance(x, y, x2, y2){
            return Math.sqrt((x2-x)^2 + (y2-y)^2)
        }
        
        dirvector(x, y, x2, y2){
            return [Math.sign(x2-x), Math.sign(y2-y)]
        }

        showpath(x, y, possibilities){
            possibilities.forEach((possibility)=>{
                this.tracepos(x, y, possibility[0], possibility[1], (block)=>{
                    if(block){
                        this.selectedblocks.push(block)
                        Activate(block.td, true, "orange");
                    }
                })
            })
        }

        traceship(x, y, w){
            
            let possibilities = [];

            CheckPlaces.forEach((dir)=>{
                
                let _x = x + (w-1) * dir[0];
                let _y = y + (w-1) * dir[1];

                let sign = -Math.sign((x+y)-(_x+_y))
                
                let traceresult = this.tracesquare(x-sign, y-sign, _x+sign, _y+sign, (hitblock, start, final)=>{
                    if(hitblock){
                        if(hitblock.name != "water"){
                           return false
                        }
                    }else{
                        if((!final) && (!start)){
                            return false    
                        }
                    }
                })

                 if(traceresult){
                     possibilities.push([_x, _y, dir]);
                 }
            })
            
            if(possibilities.length > 0){
                return possibilities;
            }else{
                return false;
            }
        }
        
        tracesquare(x, y, x2, y2, func){

                let len_y = y2-y
                let len_x = x2-x

                for (let _y=0; _y<Math.abs(len_y)+1; _y++){
                    for (let _x=0; _x<Math.abs(len_x)+1; _x++){

                        let isstart = (_y == 0 || _x == 0);
                        let isend   =  ( (_x >= Math.abs(len_x) && Math.abs(len_x) > 1 ) || (_y >= Math.abs(len_y) && Math.abs(len_y) > 1))
                        let result  = func(this.getpos(x + _x * Math.sign(len_x), y + _y * Math.sign(len_y)), isstart, isend);

                        if(typeof result == "boolean"){
                            return result
                        }
                    }
                }

            return true
        }

        tracepos(x, y, x2, y2, func){

            if(x == x2){
                let len = y2-y
                for (let i=0; i<Math.abs(len)+1; i++){
                    let result = func(this.getpos(x, y + i * Math.sign(len)), i==Math.abs(len), i==0)
                    if(typeof result == "boolean"){
                        return result
                    }
                }

                return true
            }

            if(y == y2){
                let len = x2-x
                for (let i=0; i<Math.abs(len)+1; i++){
                    let result = func(this.getpos(x + i * Math.sign(len), y), i==Math.abs(len), i==0)
                    if(typeof result == "boolean"){
                        return result
                    }
                }

                return true
            }

            return false
        }

        set selected(block){
            if(block){
                block.selected = true
            }else{
                this._selected.selected = false
            }

            this._selected = block
        }
        
        set selectedship(ship){
            if(this._selectedship){
                Activate(this._selectedship.td, false)
            }
            if(ship){
                Activate(ship.td, true, "lime")
            }
            this._selectedship = ship
        }
        
        get selectedship(){
            return this._selectedship
        }

        get selected(){
            return this._selected
        }
    }

    var Game = class{
        constructor(w, h){
            this.started    = false
            this.playerturn = true
            this.map        = new Map(this, local_body, local_ships, "Votre Plateau",   w, h)
            this.enemymap   = new Map(this, enemy_body, enemy_ships, "Plateau adverse", w, h, true);

            this.enemy_firsthit    = undefined;
            this.enemy_firsthitdir = undefined;
            this.enemy_lasthit     = undefined;
            this.enemy_done        = false;

                 this.randomPlacement(this.enemymap);

           
        }

        checkboats(ships){
            let won = true;

            ships.forEach((ship)=>{
                if(ship.alive){
                    won = false;
                }
            })

            return won;
        }

        checkwin(){
            if(this.checkboats(this.map.ships)){
                console.log("You lost!")
                this.playerturn = true;
            }
            if(this.checkboats(this.enemymap.ships)){
                console.log("You won!")
                this.playerturn = false;
            }
        }

        computerPlay(){
            let played = false;

            while(!played){
                if(this.enemy_firsthit){

                    let x;
                    let y;
                    let vec = CheckPlaces[this.enemy_firsthitdir];

                    if(this.enemy_lasthit){
                        x = this.enemy_lasthit[0] + vec[0]
                        y = this.enemy_lasthit[1] + vec[1]
                    }else{
                        x = this.enemy_firsthit[0] + vec[0]
                        y = this.enemy_firsthit[1] + vec[1]
                    }

                    let missed = false;
                    let block = this.map.getpos(x, y);

                    if(block && block.name != "missed" && !block.hit){

                        block.click();

                        if(block.hit){
                            this.enemy_lasthit = [x, y];
                        }else{
                            if(this.enemy_done){
                                missed = true;
                            }
                            if(this.enemy_lasthit){
                                this.enemy_lasthit = undefined;
                                this.enemy_firsthitdir = (this.enemy_firsthitdir+2)%4;
                                this.enemy_done = true;
                            }else{
                                this.enemy_firsthitdir++
                            }

                            played = true;
                        }
                    }else{
                        if(this.enemy_done){
                            missed = true;
                        }
                        if(this.enemy_lasthit){
                            this.enemy_lasthit = undefined;
                            this.enemy_firsthitdir = (this.enemy_firsthitdir+2)%4;
                            this.enemy_done = true;
                        }else{
                            this.enemy_firsthitdir++
                        }
                    }

                    if(this.enemy_firsthitdir > 3 || missed){
                        this.enemy_firsthit    = undefined;
                        this.enemy_firsthitdir = undefined;
                        this.enemy_lasthit     = undefined;
                    }

                }else{
                    let block = this.randomTarget(this.map);

                    if(block.name != "missed" && !block.hit){
                        block.click();

                        if(block.hit){
                            this.enemy_firsthit = [block.x, block.y];
                            this.enemy_firsthitdir = 0;
                            this.enemy_done = false;
                        }else{
                            played = true;
                        }
                    }
                }
            }
        }

        switchTurn(){
            this.playerturn = !this.playerturn;

            console.log("turn: " + (this.playerturn ? "Player" : "Computer"));

            if(!this.playerturn){
                this.computerPlay();
            }
        }

        randomPlacement(map){
            map.ships.forEach((ship)=>{
                while(!ship.placed){
                    let x = Math.floor(Math.random() * map.width) + 1;
                    let y = Math.floor(Math.random() * map.height) + 1;

                    let places = map.traceship(x, y, ship.length);

                    if(places){
                        let place = places[Math.floor(Math.random()*places.length)];

                        ship.place(x, y, place[0], place[1], place[2])
                    }
                }
            })
        }

        randomTarget(map){
            let x = Math.floor(Math.random() * map.width) + 1;
            let y = Math.floor(Math.random() * map.height) + 1;

            return map.getpos(x, y);
        }
    }

    let bruh = new Game(10,10)
}