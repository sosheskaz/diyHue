from functions.core import nextFreeId
import configManager
import HueObjects
from datetime import datetime
bridgeConfig = configManager.bridgeConfig.yaml_config

def addTradfriDimmer(sensor_id, group_id):
    rules = [{ "actions":[{"address": "/groups/" + group_id + "/action", "body":{ "on":True, "bri":1 }, "method": "PUT" }], "conditions":[{ "address": "/sensors/" + sensor_id + "/state/lastupdated", "operator": "dx"}, { "address": "/sensors/" + sensor_id + "/state/buttonevent", "operator": "eq", "value": "2002" }, { "address": "/groups/" + group_id + "/state/any_on", "operator": "eq", "value": "false" }], "name": "Remote " + sensor_id + " turn on" },{"actions":[{"address":"/groups/" + group_id + "/action", "body":{ "on": False}, "method":"PUT"}], "conditions":[{ "address": "/sensors/" + sensor_id + "/state/lastupdated", "operator": "dx" }, { "address": "/sensors/" + sensor_id + "/state/buttonevent", "operator": "eq", "value": "4002" }, { "address": "/groups/" + group_id + "/state/any_on", "operator": "eq", "value": "true" }, { "address": "/groups/" + group_id + "/action/bri", "operator": "eq", "value": "1"}], "name":"Dimmer Switch " + sensor_id + " off"}, { "actions":[{ "address": "/groups/" + group_id + "/action", "body":{ "on":False }, "method": "PUT" }], "conditions":[{ "address": "/sensors/" + sensor_id + "/state/lastupdated", "operator": "dx" }, { "address": "/sensors/" + sensor_id + "/state/buttonevent", "operator": "eq", "value": "3002" }, { "address": "/groups/" + group_id + "/state/any_on", "operator": "eq", "value": "true" }, { "address": "/groups/" + group_id + "/action/bri", "operator": "eq", "value": "1"}], "name": "Remote " + sensor_id + " turn off" }, { "actions": [{"address": "/groups/" + group_id + "/action", "body":{"bri_inc": 32, "transitiontime": 9}, "method": "PUT" }], "conditions": [{ "address": "/groups/" + group_id + "/state/any_on", "operator": "eq", "value": "true" },{ "address": "/sensors/" + sensor_id + "/state/buttonevent", "operator": "eq", "value": "2002" }, {"address": "/sensors/" + sensor_id + "/state/lastupdated", "operator": "dx"}], "name": "Dimmer Switch " + sensor_id + " rotate right"}, { "actions": [{"address": "/groups/" + group_id + "/action", "body":{"bri_inc": 56, "transitiontime": 9}, "method": "PUT" }], "conditions": [{ "address": "/groups/" + group_id + "/state/any_on", "operator": "eq", "value": "true" },{ "address": "/sensors/" + sensor_id + "/state/buttonevent", "operator": "eq", "value": "1002" }, {"address": "/sensors/" + sensor_id + "/state/lastupdated", "operator": "dx"}], "name": "Dimmer Switch " + sensor_id + " rotate fast right"}, {"actions": [{"address": "/groups/" + group_id + "/action", "body": {"bri_inc": -32, "transitiontime": 9}, "method": "PUT"}], "conditions": [{ "address": "/groups/" + group_id + "/action/bri", "operator": "gt", "value": "1"},{"address": "/sensors/" + sensor_id + "/state/buttonevent", "operator": "eq", "value": "3002"}, {"address": "/sensors/" + sensor_id + "/state/lastupdated", "operator": "dx"}], "name": "Dimmer Switch " + sensor_id + " rotate left"}, {"actions": [{"address": "/groups/" + group_id + "/action", "body": {"bri_inc": -56, "transitiontime": 9}, "method": "PUT"}], "conditions": [{ "address": "/groups/" + group_id + "/action/bri", "operator": "gt", "value": "1"},{"address": "/sensors/" + sensor_id + "/state/buttonevent", "operator": "eq", "value": "4002"}, {"address": "/sensors/" + sensor_id + "/state/lastupdated", "operator": "dx"}], "name": "Dimmer Switch " + sensor_id + " rotate left"}]
    resourcelinkId = nextFreeId(bridgeConfig, "resourcelinks")

    owner = bridgeConfig["apiUsers"][list(bridgeConfig["apiUsers"])[0]]
    bridgeConfig["resourcelinks"][resourcelinkId] = HueObjects.ResourceLink({"id_v1": resourcelinkId, "classid": 15555,"description": "Rules for sensor " + sensor_id, "links": ["/" + bridgeConfig["sensors"][sensor_id].getObjectPath()["resource"] + "/" + bridgeConfig["sensors"][sensor_id].getObjectPath()["id"]
    ], "name": "Emulator rules " + sensor_id,"owner": owner})
    for rule in rules:
        ruleId = nextFreeId(bridgeConfig, "rules")
        data = rule
        data.update({"id_v1": ruleId, "owner": owner, "recycle": True})
        bridgeConfig["rules"][ruleId] = HueObjects.Rule(data)
        bridgeConfig["resourcelinks"][resourcelinkId].add_link(bridgeConfig["rules"][ruleId])

def addTradfriCtRemote(sensor_id, group_id):
    rules = [{"actions": [{"address": "/groups/" + group_id + "/action","body": {"on": True},"method": "PUT"}],"conditions": [{"address": "/sensors/" + sensor_id + "/state/lastupdated","operator": "dx"},{"address": "/sensors/" + sensor_id + "/state/buttonevent","operator": "eq","value": "1002"},{"address": "/groups/" + group_id + "/state/any_on","operator": "eq","value": "false"}],"name": "Remote " + sensor_id + " button on"}, {"actions": [{"address": "/groups/" + group_id + "/action","body": {"on": False},"method": "PUT"}],"conditions": [{"address": "/sensors/" + sensor_id + "/state/lastupdated","operator": "dx"},{"address": "/sensors/" + sensor_id + "/state/buttonevent","operator": "eq","value": "1002"},{"address": "/groups/" + group_id + "/state/any_on","operator": "eq","value": "true"}],"name": "Remote " + sensor_id + " button off"},{ "actions": [{ "address": "/groups/" + group_id + "/action", "body": { "bri_inc": 30, "transitiontime": 9 }, "method": "PUT" }], "conditions": [{ "address": "/sensors/" + sensor_id + "/state/buttonevent", "operator": "eq", "value": "2002" }, { "address": "/sensors/" + sensor_id + "/state/lastupdated", "operator": "dx" }], "name": "Dimmer Switch " + sensor_id + " up-press" }, { "actions": [{ "address": "/groups/" + group_id + "/action", "body": { "bri_inc": 56, "transitiontime": 9 }, "method": "PUT" }], "conditions": [{ "address": "/sensors/" + sensor_id + "/state/buttonevent", "operator": "eq", "value": "2001" }, { "address": "/sensors/" + sensor_id + "/state/lastupdated", "operator": "dx" }], "name": "Dimmer Switch " + sensor_id + " up-long" }, { "actions": [{ "address": "/groups/" + group_id + "/action", "body": { "bri_inc": -30, "transitiontime": 9 }, "method": "PUT" }], "conditions": [{ "address": "/sensors/" + sensor_id + "/state/buttonevent", "operator": "eq", "value": "3002" }, { "address": "/sensors/" + sensor_id + "/state/lastupdated", "operator": "dx" }], "name": "Dimmer Switch " + sensor_id + " dn-press" }, { "actions": [{ "address": "/groups/" + group_id + "/action", "body": { "bri_inc": -56, "transitiontime": 9 }, "method": "PUT" }], "conditions": [{ "address": "/sensors/" + sensor_id + "/state/buttonevent", "operator": "eq", "value": "3001" }, { "address": "/sensors/" + sensor_id + "/state/lastupdated", "operator": "dx" }], "name": "Dimmer Switch " + sensor_id + " dn-long" }, { "actions": [{ "address": "/groups/" + group_id + "/action", "body": { "ct_inc": 50, "transitiontime": 9 }, "method": "PUT" }], "conditions": [{ "address": "/sensors/" + sensor_id + "/state/buttonevent", "operator": "eq", "value": "4002" }, { "address": "/sensors/" + sensor_id + "/state/lastupdated", "operator": "dx" }], "name": "Dimmer Switch " + sensor_id + " ctl-press" }, { "actions": [{ "address": "/groups/" + group_id + "/action", "body": { "ct_inc": 100, "transitiontime": 9 }, "method": "PUT" }], "conditions": [{ "address": "/sensors/" + sensor_id + "/state/buttonevent", "operator": "eq", "value": "4001" }, { "address": "/sensors/" + sensor_id + "/state/lastupdated", "operator": "dx" }], "name": "Dimmer Switch " + sensor_id + " ctl-long" }, { "actions": [{ "address": "/groups/" + group_id + "/action", "body": { "ct_inc": -50, "transitiontime": 9 }, "method": "PUT" }], "conditions": [{ "address": "/sensors/" + sensor_id + "/state/buttonevent", "operator": "eq", "value": "5002" }, { "address": "/sensors/" + sensor_id + "/state/lastupdated", "operator": "dx" }], "name": "Dimmer Switch " + sensor_id + " ct-press" }, { "actions": [{ "address": "/groups/" + group_id + "/action", "body": { "ct_inc": -100, "transitiontime": 9 }, "method": "PUT" }], "conditions": [{ "address": "/sensors/" + sensor_id + "/state/buttonevent", "operator": "eq", "value": "5001" }, { "address": "/sensors/" + sensor_id + "/state/lastupdated", "operator": "dx" }], "name": "Dimmer Switch " + sensor_id + " ct-long" }]
    resourcelinkId = nextFreeId(bridgeConfig, "resourcelinks")
    owner = bridgeConfig["apiUsers"][list(bridgeConfig["apiUsers"])[0]]
    bridgeConfig["resourcelinks"][resourcelinkId] = HueObjects.ResourceLink({"id_v1": resourcelinkId, "classid": 15555,"description": "Rules for sensor " + sensor_id, "links": ["/" + bridgeConfig["sensors"][sensor_id].getObjectPath()["resource"] + "/" + bridgeConfig["sensors"][sensor_id].getObjectPath()["id"]], "name": "Emulator rules " + sensor_id,"owner": owner})
    for rule in rules:
        ruleId = nextFreeId(bridgeConfig, "rules")
        data = rule
        data.update({"id_v1": ruleId, "owner": owner, "recycle": True})
        bridgeConfig["rules"][ruleId] = HueObjects.Rule(data)
        bridgeConfig["resourcelinks"][resourcelinkId].add_link(bridgeConfig["rules"][ruleId])

def addTradfriOnOffSwitch(sensor_id, group_id):
    rules = [{"actions": [{"address": "/groups/" + group_id + "/action","body": {"on": True},"method": "PUT"}],"conditions": [{"address": "/sensors/" + sensor_id + "/state/lastupdated","operator": "dx"},{"address": "/sensors/" + sensor_id + "/state/buttonevent","operator": "eq","value": "1002"}],"name": "Remote " + sensor_id + " button on"}, {"actions": [{"address": "/groups/" + group_id + "/action","body": {"on": False},"method": "PUT"}],"conditions": [{"address": "/sensors/" + sensor_id + "/state/lastupdated","operator": "dx"},{"address": "/sensors/" + sensor_id + "/state/buttonevent","operator": "eq","value": "2002"}],"name": "Remote " + sensor_id + " button off"},{ "actions": [{ "address": "/groups/" + group_id + "/action", "body": { "bri_inc": 30, "transitiontime": 9 }, "method": "PUT" }], "conditions": [{ "address": "/sensors/" + sensor_id + "/state/buttonevent", "operator": "eq", "value": "1001" }, { "address": "/sensors/" + sensor_id + "/state/lastupdated", "operator": "dx" }], "name": "Dimmer Switch " + sensor_id + " up-press" }, { "actions": [{ "address": "/groups/" + group_id + "/action", "body": { "bri_inc": -30, "transitiontime": 9 }, "method": "PUT" }], "conditions": [{ "address": "/sensors/" + sensor_id + "/state/buttonevent", "operator": "eq", "value": "2001" }, { "address": "/sensors/" + sensor_id + "/state/lastupdated", "operator": "dx" }], "name": "Dimmer Switch " + sensor_id + " dn-press" }]
    resourcelinkId = nextFreeId(bridgeConfig, "resourcelinks")
    owner = bridgeConfig["apiUsers"][list(bridgeConfig["apiUsers"])[0]]
    bridgeConfig["resourcelinks"][resourcelinkId] = HueObjects.ResourceLink({"id_v1": resourcelinkId, "classid": 15555,"description": "Rules for sensor " + sensor_id, "links": ["/" + bridgeConfig["sensors"][sensor_id].getObjectPath()["resource"] + "/" + bridgeConfig["sensors"][sensor_id].getObjectPath()["id"]], "name": "Emulator rules " + sensor_id,"owner": owner})
    for rule in rules:
        ruleId = nextFreeId(bridgeConfig, "rules")
        data = rule
        data.update({"id_v1": ruleId, "owner": owner, "recycle": True})
        bridgeConfig["rules"][ruleId] = HueObjects.Rule(data)
        bridgeConfig["resourcelinks"][resourcelinkId].add_link(bridgeConfig["rules"][ruleId])

def addTradfriSceneRemote(sensor_id, group_id):
    rules = [{"actions": [{"address": "/groups/" + group_id + "/action","body": {"on": True},"method": "PUT"}],"conditions": [{"address": "/sensors/" + sensor_id + "/state/lastupdated","operator": "dx"},{"address": "/sensors/" + sensor_id + "/state/buttonevent","operator": "eq","value": "1002"},{"address": "/groups/" + group_id + "/state/any_on","operator": "eq","value": "false"}],"name": "Remote " + sensor_id + " button on"}, {"actions": [{"address": "/groups/" + group_id + "/action","body": {"on": False},"method": "PUT"}],"conditions": [{"address": "/sensors/" + sensor_id + "/state/lastupdated","operator": "dx"},{"address": "/sensors/" + sensor_id + "/state/buttonevent","operator": "eq","value": "1002"},{"address": "/groups/" + group_id + "/state/any_on","operator": "eq","value": "true"}],"name": "Remote " + sensor_id + " button off"},{ "actions": [{ "address": "/groups/" + group_id + "/action", "body": { "bri_inc": 30, "transitiontime": 9 }, "method": "PUT" }], "conditions": [{ "address": "/sensors/" + sensor_id + "/state/buttonevent", "operator": "eq", "value": "2002" }, { "address": "/sensors/" + sensor_id + "/state/lastupdated", "operator": "dx" }], "name": "Dimmer Switch " + sensor_id + " up-press" }, { "actions": [{ "address": "/groups/" + group_id + "/action", "body": { "bri_inc": 56, "transitiontime": 9 }, "method": "PUT" }], "conditions": [{ "address": "/sensors/" + sensor_id + "/state/buttonevent", "operator": "eq", "value": "2001" }, { "address": "/sensors/" + sensor_id + "/state/lastupdated", "operator": "dx" }], "name": "Dimmer Switch " + sensor_id + " up-long" }, { "actions": [{ "address": "/groups/" + group_id + "/action", "body": { "bri_inc": -30, "transitiontime": 9 }, "method": "PUT" }], "conditions": [{ "address": "/sensors/" + sensor_id + "/state/buttonevent", "operator": "eq", "value": "3002" }, { "address": "/sensors/" + sensor_id + "/state/lastupdated", "operator": "dx" }], "name": "Dimmer Switch " + sensor_id + " dn-press" }, { "actions": [{ "address": "/groups/" + group_id + "/action", "body": { "bri_inc": -56, "transitiontime": 9 }, "method": "PUT" }], "conditions": [{ "address": "/sensors/" + sensor_id + "/state/buttonevent", "operator": "eq", "value": "3001" }, { "address": "/sensors/" + sensor_id + "/state/lastupdated", "operator": "dx" }], "name": "Dimmer Switch " + sensor_id + " dn-long" }, { "actions": [{ "address": "/groups/" + group_id + "/action", "body": { "scene_inc": -1 }, "method": "PUT" }], "conditions": [{ "address": "/sensors/" + sensor_id + "/state/buttonevent", "operator": "eq", "value": "4002" }, { "address": "/sensors/" + sensor_id + "/state/lastupdated", "operator": "dx" }], "name": "Dimmer Switch " + sensor_id + " ctl-press" }, { "actions": [{ "address": "/groups/" + group_id + "/action", "body": { "scene_inc": -1 }, "method": "PUT" }], "conditions": [{ "address": "/sensors/" + sensor_id + "/state/buttonevent", "operator": "eq", "value": "4001" }, { "address": "/sensors/" + sensor_id + "/state/lastupdated", "operator": "dx" }], "name": "Dimmer Switch " + sensor_id + " ctl-long" }, { "actions": [{ "address": "/groups/" + group_id + "/action", "body": { "scene_inc": 1 }, "method": "PUT" }], "conditions": [{ "address": "/sensors/" + sensor_id + "/state/buttonevent", "operator": "eq", "value": "5002" }, { "address": "/sensors/" + sensor_id + "/state/lastupdated", "operator": "dx" }], "name": "Dimmer Switch " + sensor_id + " ct-press" }, { "actions": [{ "address": "/groups/" + group_id + "/action", "body": { "scene_inc": 1 }, "method": "PUT" }], "conditions": [{ "address": "/sensors/" + sensor_id + "/state/buttonevent", "operator": "eq", "value": "5001" }, { "address": "/sensors/" + sensor_id + "/state/lastupdated", "operator": "dx" }], "name": "Dimmer Switch " + sensor_id + " ct-long" }]
    resourcelinkId = nextFreeId(bridgeConfig, "resourcelinks")
    bridgeConfig["resourcelinks"][resourcelinkId] = {"classid": 15555,"description": "Rules for sensor " + sensor_id, "links": ["/sensors/" + sensor_id], "name": "Emulator rules " + sensor_id,"owner": list(bridgeConfig["config"]["whitelist"])[0]}
    for rule in rules:
        ruleId = nextFreeId(bridgeConfig, "rules")
        bridgeConfig["rules"][ruleId] = rule
        bridgeConfig["rules"][ruleId].update({"created": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S"), "lasttriggered": None, "owner": list(bridgeConfig["config"]["whitelist"])[0], "recycle": True, "status": "enabled", "timestriggered": 0})
        bridgeConfig["resourcelinks"][resourcelinkId]["links"].append("/rules/" + ruleId)
