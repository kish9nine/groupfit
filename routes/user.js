// var MongoConnector = require('./../mongoConnector').MongoConnector;
/*
 * GET users listing.
 */

exports.list = function(mongoConnector){

  /* Example for getUsers/getGroups/getPlaylists */
  // return function(req, res) {
  // 	mongoConnector.getUsers(function(error, results) {
  // 		if (error) console.log(error);
  // 		else {
  // 			console.log(results);
  // 			res.send("respond with a resource");
		// }
  // 	});
  // }

  /* Example for findUser/findGroup/findPlaylist */
  // return function(req, res) {
  // 	mongoConnector.findUser("pandas@gmail.com", function(error, results) {
  // 	  if (error) console.log(error);
  // 	  else {
  // 	      console.log(results);
  // 		  res.send("respond with a resource");
		// }
  // 	});
  // }

  /* Example for insertUser/insertGroup/insertPlaylist */
  // return function(req, res) {
  // 	var user = {};
  // 	user["email"] = "pandaLovers@gmail.com";
  // 	mongoConnector.insertUser(user, function(error, results) {
  // 		if (error) console.log(error);
  // 		else {
  // 			res.send("respond with a resource");
		// }
  // 	});
  // }

  /* Example for updateUserGoal/updateUserGoal */
  return function(req, res) {
  	mongoConnector.updateGroupGoal("test1", "Run a lot", function(error, results) {
  		if (error) console.log(error);
  		else {
  			res.send("respond with a resource");
		}
  	});
  }

};