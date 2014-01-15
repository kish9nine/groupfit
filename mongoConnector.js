var Db = require('mongodb').Db;
var Connection = require('mongodb').Connection;
var Server = require('mongodb').Server;

// make sure you have mongo running in the background (run 'mongod' in terminal)
// db is 'groupfit'
// collections are 'Users', 'Groups', 'Playlists'
// Examples of usage in user.js
MongoConnector = function() {
  this.db = new Db('groupfit', new Server('localhost', 27017, {safe: false}));
  this.db.open(function(){});
};

// Get a collection in the db
MongoConnector.prototype.getCollection = function(coll, callback) {
  this.db.collection(coll, function(error, results) {
    if (error) {
      callback(error);
    } else {
      callback(null, results);
    }
  });
};

// Get all the Users
MongoConnector.prototype.getUsers = function(callback) {
  this.getCollection("Users", function(error, users) {
    if (error) console.log("error with getUsers");
    else {
      users.find().toArray(function(error, results) {
        if (error) console.log("getUsers has an error");
        else {
          return callback(null, results);
        }
      });
    }
  });
};

// Get all the Groups
MongoConnector.prototype.getGroups = function(callback) {
  this.getCollection("Groups", function(error, groups) {
    if (error) console.log("error with getGroups");
    else {
      groups.find().toArray(function(error, results) {
        if (error) console.log("getGroups has an error");
        else {
          return callback(null, results);
        }
      });
    }
  });
};

// Get all the Playlists
MongoConnector.prototype.getPlaylists = function(callback) {
  this.getCollection("Playlists", function(error, playlists) {
    if (error) console.log("error with getPlaylists");
    else {
      playlists.find().toArray(function(error, results) {
        if (error) console.log("getPlaylists has an error");
        else {
          return callback(null, results);
        }
      });

    }
  });
};

// find a User
MongoConnector.prototype.findUser = function(email, callback) {
  this.getCollection("Users", function(error, users) {
    if (error) console.log("error in findUser");
    else {
      var query = {};
      query["email"] = email;
      users.findOne(query, function(error, results) {
        if (error) console.log("error in findUser");
        else callback(null, results);
      });
    }
  });
}

// find a Group
MongoConnector.prototype.findGroup = function(name, callback) {
  this.getCollection("Groups", function(error, groups) {
    if (error) console.log("error in findGroup");
    else {
      var query = {};
      query["name"] = name;
      groups.findOne(query, function(error, results) {
        if (error) console.log("error in findGroup");
        else callback(null, results);
      });
    }
  });
}

// find a Playlist
MongoConnector.prototype.findPlaylist = function(name, callback) {
  this.getCollection("Playlists", function(error, playlists) {
    if (error) console.log("error in findPlaylist");
    else {
      var query = {};
      query["name"] = name;
      playlists.findOne(query, function(error, results) {
        if (error) console.log("error in findPlaylist");
        else callback(null, results);
      });
    }
  });
}

// Insert a user
// Assuming that newUser is a JSON with the correct params
MongoConnector.prototype.insertUser = function(newUser, callback) {
  this.getCollection("Users", function(error, users) {
    if (error) console.log("error in insertUser");
    else {
      users.insert(newUser, function(error, results) {
        if (error) console.log("error in insertUser");
        else callback(null, null);
      });

    }
  })
};

// Insert a group
// Assuming that newGroup is a JSON with the correct params
MongoConnector.prototype.insertGroup = function(newGroup, callback) {
  this.getCollection("Groups", function(error, groups) {
    if (error) console.log("error in insertGroup");
    else {
      groups.insert(newGroup, function(error, results) {
        if (error) console.log("error in insertGroup");
        else callback(null, null);
      });

    }
  })
};

// Insert a playlist
// Assuming that newGroup is a JSON with the correct params
MongoConnector.prototype.insertPlaylist = function(newGroup, callback) {
  this.getCollection("Playlists", function(error, playlists) {
    if (error) console.log("error in insertPlaylist");
    else {
      playlists.insert(newGroup, function(error, results) {
        if (error) console.log("error in insertPlaylist");
        else callback(null, null);
      });
    }
  })
};

// Update goal of user
// Assuming that email and newGoal are strings and the goal parameter is in the doc (even {goal: ""} is fine)
MongoConnector.prototype.updateUserGoal = function(email, newGoal, callback) {
  this.getCollection("Users", function(error, users) {
    if (error) console.log("error in updateUserGoal");
    else {
      var searchQuery = {};
      searchQuery["email"] = email;
      var innerUpdate = {};
      innerUpdate["goal"] = newGoal;
      var updateQuery = {};
      updateQuery["$set"] = innerUpdate;
      users.update(searchQuery, updateQuery, function(error, results) {
        if (error) console.log("error in updateUserGoal");
        else callback(null, results)
      });
    }
  });
};

// Update goal of group
// Assuming that name and newGoal are strings
MongoConnector.prototype.updateGroupGoal = function(name, newGoal, callback) {
  this.getCollection("Groups", function(error, groups) {
    if (error) console.log("error in updateGroupGoal");
    else {
      var searchQuery = {};
      searchQuery["name"] = name;
      var innerUpdate = {};
      innerUpdate["goal"] = newGoal;
      var updateQuery = {};
      updateQuery["$set"] = innerUpdate;
      groups.update(searchQuery, updateQuery, function(error, results) {
        if (error) console.log("error in updateGroupGsdfoal");
        else callback(null, results)
      });
    }
  });
};

// Didn't get to test the methods below this line
//-----------------------------------------------------------------------------

// Insert song into playlist
// Assuming that song and playlistName are strings and a Playlist Doc in mongo 
// has an array of songs ({name: "running music", songs: [ {songName: "Fortune Days"}, ... ]})
MongoConnector.prototype.insertSong = function(song, playlistName, callback) {
  this.getCollection("Playlists", function(error, playlists) {
    if (error) console.log("error in insertSong");
    else {
      var searchQuery = {};
      searchQuery["name"] = playlistName;
      var innerUpdate = {};
      innerUpdate["songName"] = song;
      var updateQuery = {};
      updateQuery["$push"] = innerUpdate;
      playlists.update(searchQuery, updateQuery, function(error, results) {
        if (error) console.log("error in insertSong");
        else callback(null, results);
      });

    }
  });
};

// Add a member to a group
// Assuming that userName and groupName are strings and a Group Doc in mongo
// has an array of members ({name: "Group name", members: [ {memberName: "Steph"}, ... ]})
MongoConnector.prototype.insertGroupMember = function(userName, groupName, callback) {
  this.getCollection("Groups", function(error, groups) {
    if (error) console.log("error in insertGroupMember");
    else {
      var searchQuery = {};
      searchQuery["name"] = groupName;
      var innerUpdate = {};
      innerUpdate["memberName"] = userName;
      var updateQuery = {};
      updateQuery["$push"] = innerUpdate;
      groups.update(searchQuery, updateQuery, function(error, results) {
        if (error) console.log("error in insertGroupMember");
        else callback(null, results);
      });


    }
  });
};

// Remove a member from a group
// Assuming that userName and groupName are strings and a Group Doc in mongo
// has an array of members ({name: "Group name", members: [ {memberName: "Steph"}, ... ]})
MongoConnector.prototype.removeGroupMember = function(userName, groupName, callback) {
  this.getCollection("Groups", function(error, groups) {
    if (error) console.log("error in removeGroupMember");
    else {
      var searchQuery = {};
      searchQuery["name"] = groupName;
      var innerUpdate = {};
      innerUpdate["memberName"] = userName;
      var updateQuery = {};
      updateQuery["$pull"] = innerUpdate;
      groups.update(searchQuery, updateQuery, function(error, results) {
        if (error) console.log("error in removeGroupMember");
        else callback(null, results);
      });


    }
  });
};

exports.MongoConnector = MongoConnector;