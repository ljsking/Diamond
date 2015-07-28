# coding=utf-8

import diamond.collector
import subprocess

class ShellCollector(diamond.collector.Collector):
    def get_default_config(self):
        config = super(ShellCollector, self).get_default_config()
        config.update({
            'path': 'shell',
        })
        return config

    def do_cmd(self, cmd):
        try:
            proc = subprocess.Popen(cmd,
                                    shell=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            (out, err) = proc.communicate()
        except subprocess.CalledProcessError, e:
            self.log.error("%s error launching: %s; skipping" %
                           (cmd, e))
            return None
        if proc.returncode:
            self.log.error("%s return exit value %s; skipping" %
                           (cmd, proc.returncode))
            return None
        if not out:
            self.log.info("%s return no output" % cmd)
            return None
        if err:
            self.log.error("%s return error output: %s" %
                           (cmd, err))
            return None
        return out
    def collect(self):
        scripts = self.config['scripts']
        for name in scripts:
            out = self.do_cmd(scripts[name])
            if not out:
                continue

            try:
                float(out.strip())
            except ValueError:
                self.log.error("%s returned error output: %s" %
                               (cmd, line))
                continue

            self.publish(name, float(out.strip()))
        return True
