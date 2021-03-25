
import json


a = {"bakUrl":"","waitSyncFinishAtStartup":"true","recordSql":"false","weightForSlaveRWSplit":"50","maxSqlRecordLength":"4000","switchoverTimeoutForTrans":"3000","enableCursor":"false","ndbSqlMode":"none","keyStorePass":"BB5A70F75DD5FEB214A5623DD171CEEB","processors":"16","serverId":"2","dataNodeIdleCheckPeriod":"120","password":"hotdb_config","parkPeriod":"100000","idcId":"2","maxLatencyForRWSplit":"1000","timerExecutor":"4","bakPassword":"","managerPort":"3325","waitForSlaveInFailover":"true","drBakUsername":"","idcNodeHost":"192.168.210.78:3325,192.168.210.79:3325","joinLoopSize":"1000","drUsername":"hotdb_config","enableFlowControl":"true","sqlTimeout":"3600","readOnly":"false","clusterHost":"192.168.210.137","version":"5.7.32","bak1Url":"","enableLatencyCheck":"true","instanceReadOnly":"1","checkVIPPeriod":"500","drUrl":"jdbc:mysql://192.168.210.136:3306/hotdb_config_dr_ha","frontWriteBlockTimeout":"10000","bak1Password":"","heartbeatTimeoutMs":"500","deadlockCheckPeriod":"3000","failoverAutoresetslave":"false","enableSleep":"false","ndbSqlUser":"root","statisticsUpdatePeriod":"0","latencyCheckPeriod":"500","drPassword":"hotdb_config","prefetchBatchMin":"10","clientFoundRows":"false","drBakPassword":"","clusterNetwork":"192.168.210.0/24","enableCalcite":"true","serverPort":"3323","haState":"backup","heartbeatPeriod":"2","enableXA":"false","enableWatchdog":"true","haMode":"3","enableSSL":"false","drBakUrl":"","ndbSqlAddr":"localhost:3329","errorsPermittedInTransaction":"true","clusterName":"Group_dr","timestampProxy":"0","ndbSqlVersion":"5.7.24","maxJoinSize":"10M","enableHeartbeat":"true","maxUserConnections":"4900","processorExecutor":"4","maxConnections":"5000","strategyForRWSplit":"0","bak1Username":"","maxLatencyForReadOnly":"4000","ndbVersion":"7.5.12","autoIncrement":"1","prefetchBatchMax":"10000","clusterPort":"3326","haNodeHost":"192.168.210.136:3325","enableListener":"false","joinBatchSize":"1000","allowReadConsistentInReadOnly":"0","url":"jdbc:mysql://192.168.210.78:3306/hotdb_config_dr_ha","clusterSize":"2","showAllAffectedRowsInGlobalTable":"true","prefetchBatchInit":"100","maxIdleTransactionTimeout":"86400000","keyStore":"/server.jks","dropTableRetentionTime":"0","configMGR":"false","cryptMandatory":"false","bakUsername":"","joinable":"true","VIP":"192.168.210.218","ndbSqlDataAddr":"127.0.0.1:3327","ndbSqlPass":"root","prefetchValidTimeout":"10","username":"hotdb_config"}

b = {"switchByLogInFailover":"false","skipDatatypeCheck":"false","inHeapEntrySize":20000,"waitSyncFinishAtStartup":"true","recordLimitOffsetWithoutOrderby":"false","switchoverTimeoutForTrans":3000,"checkUpdate":"true","recordMySQLErrors":"false","processors":16,"clusterElectionTimeoutMs":2000,"pingPeriod":3600,"recordSqlAuditlog":"false","unusualSQLMode":1,"highCostSqlConcurrency":32,"maxAllowedPacket":"64M","password":"hotdb_config","maxLatencyForRWSplit":1000,"idcId":2,"defaultSortedLimitSize":2000,"recordUNION":"false","evaluateNextPrefetchDuration":0,"recordSQLIntercepted":"false","crossDbXa":"false","idcNodeHost":"192.168.210.78:3325,192.168.210.79:3325","enableFlowControl":"true","maxWritingToNetTimes":120000,"readOnly":"false","skipDbNodesCheck":"false","version":"5.7.32","clusterHost":"192.168.210.137","enableLatencyCheck":"true","instanceReadOnly":1,"waitConfigSyncFinish":"false","recordAuditlog":"true","operateMode":0,"lockWaitTimeout":31536000,"frontWriteBlockTimeout":10000,"heartbeatTimeoutMs":500,"joinSize":10000000,"recordCrossDNJoin":"false","recordSubQuery":"false","failoverAutoresetslave":"false","enableSleep":"false","statisticsUpdatePeriod":0,"recordHotDBErrors":"true","defaultMaxLimit":10000,"globalUniqueConstraint":"false","versionComment":"HotDB-2.5.7 HotDB Server by Hotpu Tech","recordSQLUnsupported":"true","clientFoundRows":"false","clusterNetwork":"192.168.210.0/24","enableCalcite":"true","serverPort":3323,"enableXA":"false","enableWatchdog":"true","generatePrefetchCostRatio":90,"badConnAfterFastCheckAllIdle":"true","errorsPermittedInTransaction":"true","clusterName":"Group_dr","checkConnValid":"true","maxJoinSize":"10M","aggressive":"false","badConnAfterContinueGet":"true","checkConnLastUsedTime":3000,"maxLatencyForReadOnly":4000,"ndbVersion":"7.5.12","autoIncrement":1,"clusterPort":3326,"haNodeHost":"192.168.210.136:3325","pingLogCleanPeriod":3,"maxFlowControl":256,"url":"jdbc:mysql://192.168.210.78:3306/hotdb_config_dr_ha?&characterEncoding=UTF-8","allowRCWithoutReadConsistentInXA":0,"waitSlaveSycnWithDRMasterInFailover":"false","recordDeadLockSQL":"true","dropTableRetentionTime":0,"configMGR":"false","cryptMandatory":"false","recordMySQLWarnings":"false","prefetchValidTimeout":10000,"recordSql":"false","weightForSlaveRWSplit":50,"maxSqlRecordLength":4000,"enableCursor":"false","ndbSqlMode":"none","keyStorePass":"BB5A70F75DD5FEB214A5623DD171CEEB","checkConnValidTimeout":500,"joinCacheSize":32,"enableUnsafe":"false","serverId":2,"frontConnectionTrxIsoLevel":2,"interruptSessionWhenGCException":"false","dataNodeIdleCheckPeriod":120,"parkPeriod":100000,"ndbSqlDataSshUser":"root","timerExecutor":4,"recordSQLSyntaxError":"false","managerPort":3325,"socketBacklog":1000,"waitForSlaveInFailover":"true","enableSubquery":"true","joinLoopSize":1000,"drUsername":"hotdb_config","sqlTimeout":3600,"checkVIPPeriod":500,"checkMysqlParamInterval":600000,"clusterHeartbeatTimeoutMs":5000,"drUrl":"jdbc:mysql://192.168.210.136:3306/hotdb_config_dr_ha?&characterEncoding=UTF-8","deadlockCheckPeriod":3000,"clusterPacketTimeoutMs":5000,"ndbSqlUser":"root","recordIUDInNonXaTrx":"true","clusterStartedPacketTimeoutMs":5000,"latencyCheckPeriod":500,"drPassword":"hotdb_config","pingAbnormalPeriod":30,"pingLogCleanPeriodUnit":2,"prefetchBatchMin":10,"sslUseSM4":"false","heartbeatPeriod":2,"haState":"backup","haMode":3,"enableSSL":"false","ndbSqlAddr":"localhost:3329","timestampProxy":0,"recordHotDBWarnings":"false","ndbSqlVersion":"5.7.24","enableHeartbeat":"true","maxUserConnections":4900,"processorExecutor":4,"maxConnections":5000,"strategyForRWSplit":0,"usingAIO":0,"prefetchBatchMax":10000,"adaptiveProcessor":"true","maxReconnectConfigDBTimes":3,"enableListener":"false","joinBatchSize":1000,"recordDDL":"false","allowReadConsistentInReadOnly":0,"recordSQLKeyConflict":"false","clusterSize":2,"showAllAffectedRowsInGlobalTable":"true","recordSQLForward":"false","prefetchBatchInit":100,"enableOracleFunction":"false","maxIdleTransactionTimeout":86400000,"idleTimeout":0,"keyStore":"/server.jks","routeByRelativeCol":"false","maxNotInSubquery":20000,"joinable":"true","VIP":"192.168.210.218","ndbSqlDataAddr":"127.0.0.1:3327"}


k1 = []
k2 = []

a_keys = a.keys()
b_keys = b.keys()

for a_k in a_keys:
    if a_k in b_keys:
        k1.append(a_k)

for b_k in b_keys:
    if b_k in a_keys:
        k2.append(b_k)

keys = set(k1 + k2)

a_new = {}
b_new = {}

for k in keys:
    try:
        a_new[k] = a[k]
    except KeyError:
        pass

for k in keys:
    try:
        b_new[k] = b[k]
    except KeyError:
        pass

print(json.dumps(a_new))
print(json.dumps(b_new))