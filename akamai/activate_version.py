import json
import sys
import update_api_utilties as util

def main():
    # Authenticate with EdgeGrid
    util.initEdgeGridAuth()

    waitForActivation = False

    if len(sys.argv) > 1:
        version_to_activate = sys.argv[1]
    else:
        sys.exit("Activation failed: no property version number specified")
    
    if len(sys.argv) > 2:
        aka_env = sys.argv[2]
    else:
        aka_env = "STAGING"
    
    if len(sys.argv) > 3:
        crc_env = sys.argv[3]
    else:
        crc_env = "stage"
    
    if len(sys.argv) > 4:
        waitForActivation = (sys.argv[4].lower() == "true")
    
    previous_version = util.getLatestVersionNumber(crc_env, aka_env)
    with open("previousversion.txt", "w") as f:
        f.write(str(previous_version))

    print(">>>>>>>>>>>>>>>>>>>>>>>> Beginning activation for {} in {}! <<<<<<<<<<<<<<<<<<<<<<<<".format(crc_env, aka_env))
    print("Activating v{}".format(version_to_activate))

    # Activate on given env
    util.activateVersion(version_to_activate, aka_env, crc_env)

    # Wait, if necessary
    if waitForActivation:
        util.waitForActiveVersion(int(version_to_activate), aka_env, crc_env)


if __name__== "__main__":
    main()
