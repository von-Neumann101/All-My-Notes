 1. Openclaw architecture overview：
    微信飞书等 Channel，枢纽 Gateway，Pi Agent 运行环境，Skill，插件 Plugin，节点 Node，钩子 Hook
    作业：安装 Openclaw
    
 2. Channel:
    握手 Handshake, 心跳 Heartbeat, 消息 Message, 事件 Event, 鉴权与授权 Authentication & Authorization
    作业：安装微信和飞书 channel

 3. Gateway, part 1:
    Nodejs 运行环境, Channel 通信, 安全机制, 单机和分布式部署
    作业：Nodejs

 4. Gateway, part 2:
    Memory QMD, 复杂应用的实现
    作业：安装使用 QMD 
    
 5. Pi Agent runtime，part 1：
    多种 AI 模型接口的统一，五个冲程
    作业：使用 OpenRouter
    
 6. Pi Agent runtime，part 2：
    树状的 session log，Tool factory
    作业：使用 QMD 管理 session
 
 7. Integrate Pi with Openclaw
    从 Openclaw 进入 Pi 的入口，Pi 五个冲程中埋的坑
    作业：如何修复这几个 bugs

 8. Tool, part 1:
    Skill, docker, plugin, node
    作业：实现一个在 docker 中运行程序的 skill
    
 9. Tool, poart 2:
    复杂工具，自动编程与 ACP，浏览器操控与 CDP，外挂屏幕渲染与 A2UI
    作业：browserless 浏览器操控
    
 10. Agent team：
    多元通信 Matrix，Agent 会议室和看板 Mattermost
    作业：Mattermost 项目协同进展看板