var USERNAME = 'felix';
var GAME = 'ttt'; // s1 | catan | ttt | empty | game01 | aristocracy
var PLAYMODE = 'hotseat'; // multiplayer | hotseat | solo | passplay
var SEED = 1;
//var AI_TYPE = 'random';
const PLAYER_CONFIG_FOR_MULTIPLAYER = ['me', 'human', 'human'];

const USE_LOCAL_STORAGE = false; // true | false

//ONLY used when *** NOT testing: ***
const VERSION = '_ui'; //files sollen heissen [GAME]_01.yaml and [GAME]_01.js, und im richtigen dir sein!!
const CACHE_DEFAULTSPEC = false;
const CACHE_USERSPEC = false;
const CACHE_CODE = false;
const CACHE_INITDATA = true;

//*** TESTING *** uses files in /tests/GAME/uspecN and codeN, NO caching of uspec, code, and data!
//const TESTING = false; // true | false //uses files from tests, DOES NOT send routes to server, instead: server stub
const RUNTEST = false; // true | false //just runTest preprocess serverData, pageHeaderInit, and clear
const USE_NON_TESTING_DATA = true;

const DSPEC_VERSION = 3;
const USPEC_VERSION = '2a';
const CODE_VERSION = 1;
const SERVERDATA_VERSION = 1;
const TEST_PATH = '/zdata/';

//might change but unlikely:
const INIT_CLEAR_LOCALSTORAGE = true; // true | false //tru will delete complete localStorage at _startSession
const USE_MAX_PLAYER_NUM = false; // true | false
const STARTING_TAB_OPEN = 'bPlayers'; // bObjects | bPlayers | bSettings
const TIMIT_SHOW = false; // true | false
const SHOW_SERVER_ROUTE = false; // true | false
const SHOW_SERVER_RETURN = false; // true | false
const SHOW_CODE_DATA = false; // true | false
const SHOW_SPEC = true; // true | false
const USE_OLD_GRID_FUNCTIONS = false;// true | false
const USE_ALL_GAMES_ROUTE = false; //set true if route /game/info works again! if false loads info.yaml directly

//#region cache options
// 
// const CACHE_ASSETS = true; // true | false
// const CACHE_DEFAULT_SPEC_CODE = false; // true | false
// const CACHE_SERVERDATA = false; // true | false

//#region server options
const USE_SOCKETIO = false;
const USE_BACKEND_AI = true;
const IS_MIRROR = false;
const FLASK = true;
const PORT = '5000';
const NGROK = null;// 'http://ee91c9fa.ngrok.io/'; // null;//'http://f3629de0.ngrok.io/'; //null; //'http://b29082d5.ngrok.io/' //null; //'http://2d97cdbd.ngrok.io/';// MUSS / am ende!!! 
const SERVER_URL = IS_MIRROR ? 'http://localhost:5555/' : FLASK ? (NGROK ? NGROK : 'http://localhost:' + PORT + '/') : 'http://localhost:5005/';
const SERVER = 'http://localhost:5000'

//general settings: 
var S_tooltips = 'OFF';
var S_openTab = 'CodeTab'; // SpecTab | CodeTab | ObjectsTab | SettingsTab

var S_useSimpleCode = false; // true | false
var S_userSettings = true; // true | false
var S_userStructures = true; // true | false
var S_userBehaviors = true; // true | false

var S_autoplay = false;
var S_showEvents = false; //unused
var S_AIThinkingTime = 30;
var S_autoplayFunction = (_g) => false;//_g.phase == 'setup';// false; //counters.msg < 25; //counters.msg < 13; // false; //G.player!='White' && G.player != 'Player1';

//rsg settings
var S_boardDetection = true; //if no spec per default use board detection
var S_deckDetection = true; //if no spec per default use board detection
var S_useColorHintForProperties = true; //color hint used as foreground when writing prop vals on object
var S_useColorHintForObjects = true;//color hint used as background when creating new objects (eg., road)
var S_defaultObjectArea = 'a_d_objects';
var S_defaultPlayerArea = 'a_d_players';

//other stuff
const names = ['felix', 'amanda', 'sabine', 'tom', 'taka', 'microbe', 'dwight', 'jim', 'michael', 'pam', 'kevin', 'darryl', 'lauren', 'anuj', 'david', 'holly'];
var view = null;
var isPlaying = false; //initially
var isReallyMultiplayer = false;

function gcsAuto() {
	//automatically set a player configuration when starting in game view
	gcs = {};
	for (const gName in allGames) {
		let info = allGames[gName]
		//console.log(gName, info);
		let nPlayers = info.num_players[0]; // min player number, info.num_players.length - 1]; // max player number
		let pls = [];
		for (let i = 0; i < nPlayers; i++) {
			let pl = { id: info.player_names[i], playerType: 'me', agentType: null, username: USERNAME + (i > 0 ? i : '') };
			//console.log('player:', pl)
			pls.push(pl);
		}
		gcs[gName] = { numPlayers: nPlayers, players: pls };

	}
	//console.log('-------------------',gcs);
}

//#region shortcut for game player configuration (unused!)
var gcs = {
	ttt: {
		numPlayers: 2,
		players: [
			{ id: 'Player1', playerType: 'me', agentType: null, username: USERNAME },
			{ id: 'Player2', playerType: 'me', agentType: null, username: USERNAME + '1' },
		]
	},
	s1: {
		numPlayers: 4,
		players: [
			{ id: 'Player1', playerType: 'me', agentType: null, username: USERNAME },
			{ id: 'Player2', playerType: 'me', agentType: null, username: USERNAME + '1' },
			{ id: 'Player3', playerType: 'me', agentType: null, username: USERNAME + '2' },
			{ id: 'Player4', playerType: 'me', agentType: null, username: USERNAME + '3' },
		]
	},
	starter: {
		numPlayers: 2,
		players: [
			{ id: 'Player1', playerType: 'me', agentType: null, username: USERNAME },
			{ id: 'Player2', playerType: 'me', agentType: null, username: USERNAME + '1' },
		]
	},
	aristocracy: {
		numPlayers: 2,
		players: [
			{ id: 'Player1', playerType: 'me', agentType: null, username: USERNAME },
			{ id: 'Player2', playerType: 'me', agentType: null, username: USERNAME + '1' },
		]
	},
	catan: {
		numPlayers: 3,
		players: [
			{ id: 'White', playerType: 'me', agentType: null, username: USERNAME },
			{ id: 'Red', playerType: 'me', agentType: null, username: USERNAME + '1' },
			{ id: 'Blue', playerType: 'me', agentType: null, username: USERNAME + '2' },
			// { id: 'Red', playerType: 'AI', agentType: 'regular', username: 'bot0' },
			// { id: 'Blue', playerType: 'AI', agentType: 'random', username: 'bot1' },
		]
	}
}
//#endregion
